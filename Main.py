import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

# Imports UIs
from Configuration_Screen import ConfigurationScreen
from views.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Screens
        configuration_tab = ConfigurationScreen()
        self.tabWidget.addTab(configuration_tab, "Configurações")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
