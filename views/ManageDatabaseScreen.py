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

    def fill_database_list(self):
        self.databaseList.clear()
        self.databaseList.addItems(self.database_list)



