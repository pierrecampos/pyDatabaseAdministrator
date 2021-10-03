from PyQt5.QtWidgets import QWidget, QPushButton

import Utils
from views.ConfigurationScreenUI import Ui_Configuration


class ConfigurationScreen(QWidget, Ui_Configuration):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        Utils.set_event_to_buttons(self.groupProject, QPushButton, lambda: print("ok"))

