import asyncio
import os

import fdb
import psutil
from fdb import Error

from model.Constants import Constants
from util.SampleFile import SampleFiles


class FirebirdUtils:

    @staticmethod
    def test_connection(dsn, port):
        try:
            fdb.connect(dsn, user='sysdba', password='masterkey', port=port)
            return True
        except Error:
            return False

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
            connected = cls.test_connection(dsn, port)
        elif firebird == Constants.FIREBIRD3_0:
            connected = cls.test_connection(dsn, port)

        return connected

    @staticmethod
    def build_firebird_file_conf(configurator, firebird_version):
        file_content = SampleFiles.BASE_CONF
        file_content = file_content.replace(SampleFiles.BASE_CONF_ALIAS, configurator.database_client_path)

        if firebird_version == Constants.FIREBIRD2_5:
            file_content = file_content.replace(SampleFiles.LOG_ALIAS, configurator.log_2_5_path)
        else:
            file_content = file_content.replace(SampleFiles.LOG_ALIAS, configurator.log_3_0_path)

        return file_content
