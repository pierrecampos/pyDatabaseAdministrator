from PyQt5.QtWidgets import QWidget

from views.ui.ManageDatabaseScreenUI import Ui_ManageDatabaseScreen


class ManageDatabaseScreen(QWidget, Ui_ManageDatabaseScreen):
    def __init__(self, parent, configuration):
        super().__init__(parent)
        super().setupUi(self)
        self.conf = configuration
