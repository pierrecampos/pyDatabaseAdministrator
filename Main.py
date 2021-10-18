import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

# Imports UIs
from model.Configuration import Configuration
from util.FileManager import FileManager
from views.ConfigurationScreen import ConfigurationScreen
from views.InfoScreen import InfoScreen
from views.ManageDatabaseScreen import ManageDatabaseScreen
from views.ui.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QtGui.QIcon('pi.png'))
        self.fm = FileManager()
        self.configuration = Configuration(self.fm.get_attributes_from_config_file())

        # Screens
        md_tab = ManageDatabaseScreen(None, self.configuration)
        conf_tab = ConfigurationScreen(None, self.configuration, md_tab.update_database_list)
        info_tab = InfoScreen(None)

        self.tabWidget.addTab(md_tab, "Administrar Bancos")
        self.tabWidget.addTab(conf_tab, "Configurações")
        self.tabWidget.addTab(info_tab, "Sobre")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
