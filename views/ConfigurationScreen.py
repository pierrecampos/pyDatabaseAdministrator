from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit

from util import Utils
from model.Configuration import Configuration
from util.CustomExceptions import ExceptionSaveFields
from util.DialogsHelper import DialogsHelper
from util.FileManager import FileManager
from views.ui.ConfigurationScreenUI import Ui_Configuration


class ConfigurationScreen(QWidget, Ui_Configuration):
    def __init__(self, parent=None, configuration=None):
        super().__init__(parent)
        super().setupUi(self)
        self.conf = configuration
        Utils.set_event_to_buttons(self, QPushButton, self.button_events)
        self.set_regex_firebird_ports()
        self.object_to_screen()

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
            self.save_settings()

    def save_settings(self):
        try:
            self.screen_to_object()
            self.validate_fields()
            FileManager.save_config_file(self.conf.get_attributes())
        except ExceptionSaveFields as err:
            DialogsHelper.show_info(self, 'Atenção', err.message)

    def set_regex_firebird_ports(self):
        regex = QRegExp("[0-9]{8}")
        self.txtFirebirdPort2_5.setValidator(QRegExpValidator(regex))
        self.txtFirebirdPort3_0.setValidator(QRegExpValidator(regex))

    def screen_to_object(self):
        attributes = dict()
        attributes["databases_path"] = self.txtDatabasesPath.text()
        attributes["local_xml_path"] = self.txtLocalXml.text()
        attributes["log2_5_path"] = self.txtLog2_5.text()
        attributes["log3_0_path"] = self.txtLog3_0.text()
        attributes["database_nfe_path"] = self.txtDatabaseNFE.text()
        attributes["version_path"] = self.txtVersion.text()
        attributes["address_path"] = self.txtAddress.text()
        attributes["firebird2_5_path"] = self.txtFirebird2_5.text()
        attributes["firebird3_0_path"] = self.txtFirebird3_0.text()
        attributes["port_firebird2_5"] = self.txtFirebirdPort2_5.text()
        attributes["port_firebird3_0"] = self.txtFirebirdPort3_0.text()
        self.conf.set_attributes(attributes)

    def object_to_screen(self):
        self.txtDatabasesPath.setText(self.conf.databases_path)
        self.txtLocalXml.setText(self.conf.local_xml_path)
        self.txtLog2_5.setText(self.conf.log2_5_path)
        self.txtLog3_0.setText(self.conf.log3_0_path)
        self.txtDatabaseNFE.setText(self.conf.database_nfe_path)
        self.txtVersion.setText(self.conf.version_path)
        self.txtAddress.setText(self.conf.address_path)
        self.txtFirebird2_5.setText(self.conf.firebird2_5_path)
        self.txtFirebird3_0.setText(self.conf.firebird3_0_path)
        self.txtFirebirdPort2_5.setText(self.conf.port_firebird2_5)
        self.txtFirebirdPort3_0.setText(self.conf.port_firebird3_0)

    def validate_fields(self):
        txt_values = dict()
        for txt in self.findChildren(QLineEdit):
            key = str(txt.objectName())
            value = str(txt.text()).strip()
            if not value:
                raise ExceptionSaveFields('Preencha todos os campos antes de salvar !')
            txt_values[key] = value
