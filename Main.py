import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

# Imports UIs
from model.Configuration import Configuration
from views.ConfigurationScreen import ConfigurationScreen
from util.FileManager import FileManager
from views.ManageDatabaseScreen import ManageDatabaseScreen
from views.ui.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.fm = FileManager()
        self.configuration = Configuration(self.fm.get_attributes_from_config_file())

        # Screens
        manage_database_tab = ManageDatabaseScreen(None, self.configuration)
        configuration_tab = ConfigurationScreen(None, self.configuration)

        self.tabWidget.addTab(manage_database_tab, "Administrar Bancos")
        self.tabWidget.addTab(configuration_tab, "Configurações")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
