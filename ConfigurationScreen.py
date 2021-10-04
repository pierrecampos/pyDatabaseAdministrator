from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QPushButton

import Utils
from views.ConfigurationScreenUI import Ui_Configuration


class ConfigurationScreen(QWidget, Ui_Configuration):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        Utils.set_event_to_buttons(self, QPushButton, self.button_events)
        self.set_regex_firebird_ports()

    def button_events(self):
        sender = self.sender()
        path = ''
        if sender == self.btnDatabasePath:
            path = Utils.get_folder_path(self)
            self.txtDatabasesPath.setText(path)
        elif sender == self.btnLocalXml:
            path = Utils.get_file_path(self, 'local.xml')
            self.txtLocalXml.setText(path)
        elif sender == self.btnLog2_5:
            path = Utils.get_file_path(self, '*.fdb')
            self.txtLog2_5.setText(path)
        elif sender == self.btnLog3_0:
            path = Utils.get_file_path(self, '*.fdb')
            self.txtLog3_0.setText(path)
        elif sender == self.btnDatabaseNFE:
            path = Utils.get_file_path(self, '*.fdb')
            self.txtDatabaseNFE.setText(path)
        elif sender == self.btnVersion:
            path = Utils.get_folder_path(self)
            self.txtVersion.setText(path)
        elif sender == self.btnAddress:
            path = Utils.get_folder_path(self)
            self.txtAddress.setText(path)
        elif sender == self.btnFirebirdPath2_5:
            path = Utils.get_folder_path(self)
            self.txtFirebird2_5.setText(path)
        elif sender == self.btnFirebirdPath3_0:
            path = Utils.get_folder_path(self)
            self.txtFirebird3_0.setText(path)
        elif sender == self.btnSaveSettings:
            print("SAVE!")

    def set_regex_firebird_ports(self):
        regex = QRegExp("[0-9]{8}")
        self.txtFirebirdPort2_5.setValidator(QRegExpValidator(regex))
        self.txtFirebirdPort3_0.setValidator(QRegExpValidator(regex))

