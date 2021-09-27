from PyQt5.QtWidgets import QWidget

from views.ConfigurationScreenUI import Ui_Configuration


class ConfigurationScreen(QWidget, Ui_Configuration):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
