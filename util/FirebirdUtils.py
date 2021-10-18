import asyncio
import os

import fdb
import psutil
from fdb import Error

from model.Constants import Constants
from util.FolderManager import FolderManager
from util.SampleFile import SampleFiles
from util.Utils import Utils


class FirebirdUtils:

    @staticmethod
    def get_connection(dsn, port):
        try:
            connection = fdb.connect(dsn, user='sysdba', password='masterkey', port=port)
            return connection
        except Error:
            return None

    @classmethod
    def discover_connection(cls, database, configurator):
        dsn = database.path
        port2_5 = configurator.port_firebird2_5
        port3_0 = configurator.port_firebird3_0
        connected = False
        firebird_version = None

        if cls.firebird_3_0_running():
            connected = cls.discover_firebird(Constants.FIREBIRD3_0, dsn, port3_0)
            firebird_version = Constants.FIREBIRD3_0
            if not connected:
                asyncio.run(cls.kill_firebird_3_0())
                connected = cls.discover_firebird(Constants.FIREBIRD2_5, dsn, port2_5)
                firebird_version = Constants.FIREBIRD2_5
        else:
            connected = cls.discover_firebird(Constants.FIREBIRD2_5, dsn, port2_5)
            firebird_version = Constants.FIREBIRD2_5
            if not connected:
                asyncio.run(cls.start_firebird_3_0(configurator))
                connected = cls.discover_firebird(Constants.FIREBIRD3_0, dsn, port3_0)
                firebird_version = Constants.FIREBIRD3_0
        return connected, firebird_version

    @staticmethod
    def firebird_3_0_running():
        return "firebird.exe" in (p.name() for p in psutil.process_iter())

    @classmethod
    async def start_firebird_3_0(cls, configurator):
        if cls.firebird_3_0_running():
            return

        command = 'cd  ' + configurator.firebird3_0_path + ' && start firebird -a'
        os.system(command)
        await asyncio.sleep(1)

    @classmethod
    async def kill_firebird_3_0(cls):
        if cls.firebird_3_0_running():
            os.system('taskkill /im firebird.exe -f')
            await asyncio.sleep(1)

    @classmethod
    def discover_firebird(cls, firebird, dsn, port):
        connected = False
        if firebird == Constants.FIREBIRD2_5:
            connected = cls.get_connection(dsn, port)
        elif firebird == Constants.FIREBIRD3_0:
            connected = cls.get_connection(dsn, port)

        return connected is not None

    @staticmethod
    def build_firebird_file_conf(configurator, firebird_version, database):
        file_content = SampleFiles.BASE_CONF
        file_content = file_content.replace(SampleFiles.BASE_CONF_ALIAS, FolderManager.fix_path(database.path))
        file_content = file_content.replace(SampleFiles.NFE_ALIAS,
                                            FolderManager.fix_path(configurator.database_nfe_path))
        file_content = file_content.replace(SampleFiles.VERSION_ALIAS,
                                            FolderManager.fix_path(configurator.version_path))
        file_content = file_content.replace(SampleFiles.ADDRESS_ALIAS,
                                            FolderManager.fix_path(configurator.address_path))

        if firebird_version == Constants.FIREBIRD2_5:
            file_content = file_content.replace(SampleFiles.LOG_ALIAS, FolderManager.fix_path(configurator.log2_5_path))
        else:
            file_content = file_content.replace(SampleFiles.LOG_ALIAS, FolderManager.fix_path(configurator.log3_0_path))

        return file_content

    @staticmethod
    def get_default_firebird_file_path(configurator, firebird_version):
        path = ''
        if firebird_version == Constants.FIREBIRD2_5:
            path = os.path.join(configurator.firebird2_5_path, Constants.FIREBIRD2_5_CONF_NAME)
        else:
            path = os.path.join(configurator.firebird3_0_path, Constants.FIREBIRD3_0_CONF_NAME)
        return FolderManager.fix_path(path)

    @classmethod
    def get_version_from_database(cls, dsn, port):
        connection = cls.get_connection(dsn, port)
        version = '-'
        if connection is not None:
            cursor = connection.cursor()
            select = 'Select Max(V.codigo) Version From Versao V'
            result = cursor.execute(select)
            version = str(result.fetchone()[0])
        return '-' if version is None else Utils.format_version_database(version)
