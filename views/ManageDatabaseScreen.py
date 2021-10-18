from PyQt5.QtWidgets import QWidget

from model.Constants import Constants
from util.CustomExceptions import ExceptionSaveFile
from util.DialogsHelper import DialogsHelper
from util.FirebirdUtils import FirebirdUtils
from util.FolderManager import FolderManager
from util.Utils import Utils
from views.ui.ManageDatabaseScreenUI import Ui_ManageDatabaseScreen


class ManageDatabaseScreen(QWidget, Ui_ManageDatabaseScreen):
    def __init__(self, parent, configuration):
        super().__init__(parent)
        super().setupUi(self)
        self.conf = configuration
        self.database_list = FolderManager.get_folders(self.conf.databases_path)
        self.fill_database_list()
        self.databaseList.doubleClicked.connect(self.set_database)
        self.txtFilterDatabase.textChanged.connect(self.apply_filter)

    def set_database(self):
        selected_database_name = self.databaseList.currentItem().text()
        database = self.database_list[selected_database_name]
        connected, firebird_version = FirebirdUtils.discover_connection(database, self.conf)
        if not connected:
            self.set_status(connected, firebird_version, selected_database_name)
            DialogsHelper.show_warning(self, "Conexão",
                                       "Não foi possível se conectar ao banco " + selected_database_name)
            return

        try:
            firebird_conf = FirebirdUtils.build_firebird_file_conf(self.conf, firebird_version, database)
            firebird_conf_path = FirebirdUtils.get_default_firebird_file_path(self.conf, firebird_version)
            Utils.write_file(firebird_conf, firebird_conf_path)

            local_xml = Utils.build_local_xml(self.conf, firebird_version)
            Utils.write_file(local_xml, self.conf.local_xml_path)
        except ExceptionSaveFile as err:
            DialogsHelper.show_error(self, "Error", err.message)
            return

        self.set_status(connected, firebird_version, selected_database_name)

    def fill_database_list(self, filtered_folders=None):
        self.databaseList.clear()
        self.databaseList.addItems(self.database_list if filtered_folders is None else filtered_folders)

    def apply_filter(self):
        filtered_folders = Utils.filter_list(self.database_list, self.txtFilterDatabase.text())
        self.fill_database_list(filtered_folders)

    def update_database_list(self):
        self.database_list = FolderManager.get_folders(self.conf.databases_path)
        self.fill_database_list()

    def set_status(self, connected, firebird_version, database):
        if connected:
            self.lblConnectionStatus.setText('Conectado')
            self.lblConnectionStatus.setStyleSheet('color:green;')
        else:
            self.lblConnectionStatus.setText('Desconectado')
            self.lblConnectionStatus.setStyleSheet('color:red;')

        self.lblDatabaseConnected.setText(database)
        self.lblDatabaseVersion.setText('-')
        self.lblFirebirdVersion.setText(Constants.get_version_string(firebird_version))
