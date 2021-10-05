import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

# Imports UIs
from ConfigurationScreen import ConfigurationScreen
from FileManager import FileManager
from views.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.fm = FileManager()

        # Screens
        configuration_tab = ConfigurationScreen(None, self.fm.get_attributes_from_config_file())
        self.tabWidget.addTab(configuration_tab, "Configurações")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
