from PyQt5.QtWidgets import QWidget

from util.FolderManager import FolderManager
from views.ui.ManageDatabaseScreenUI import Ui_ManageDatabaseScreen


class ManageDatabaseScreen(QWidget, Ui_ManageDatabaseScreen):
    def __init__(self, parent, configuration):
        super().__init__(parent)
        super().setupUi(self)
        self.conf = configuration
        self.database_list = FolderManager.get_folders(self.conf.databases_path)
        self.fill_database_list()
        self.databaseList.doubleClicked.connect(self.set_database)

    def set_database(self):
        selected_database_name = self.databaseList.currentItem().text()
        database = self.database_list[selected_database_name]


        
    def fill_database_list(self):
        self.databaseList.clear()
        self.databaseList.addItems(self.database_list)

    def update_database_list(self):
        self.database_list = FolderManager.get_folders(self.conf.databases_path)
        self.fill_database_list()
