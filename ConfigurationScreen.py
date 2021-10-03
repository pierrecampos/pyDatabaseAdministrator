from PyQt5.QtWidgets import QWidget, QPushButton

import Utils
from views.ConfigurationScreenUI import Ui_Configuration


class ConfigurationScreen(QWidget, Ui_Configuration):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        Utils.set_event_to_buttons(self.groupProject, QPushButton, self.button_events)

    def button_events(self):
        sender = self.sender()
        if sender == self.btnDatabasePath:
            pass
        elif sender == self.btnLocalXml:
            pass
        elif sender == self.btnLog2_5:
            pass
        elif sender == self.btnLog3_0:
            pass
        elif sender == self.btnDatabaseNFE:
            pass
        elif sender == self.btnVersion:
            pass
        elif sender == self.txtAddress:
            pass
        elif sender == self.btnFirebirdPath2_5:
            pass
        elif sender == self.btnFirebirdPath3_0:
            pass
        elif sender == self.btnSaveSettings:
            pass
