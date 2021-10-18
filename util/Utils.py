from PyQt5.QtWidgets import QFileDialog

from model.Constants import Constants
from util.CustomExceptions import ExceptionSaveFile
from util.SampleFile import SampleFiles


class Utils:
    pass

    @staticmethod
    def set_event_to_buttons(father, type_object, func):
        for item in father.findChildren(type_object):
            item.clicked.connect(func)

    @staticmethod
    def get_folder_path(central_widget):
        path = QFileDialog.getExistingDirectory(central_widget, 'Procurar')
        return path

    @staticmethod
    def get_file_path(central_widget, file_filter=''):
        path, _ = QFileDialog.getOpenFileName(central_widget, 'Procurar ' + file_filter, '', file_filter)
        return path

    @staticmethod
    def build_local_xml(configurator, firebird_version):
        file_content = SampleFiles.LOCAL_XML
        port = ''
        if firebird_version == Constants.FIREBIRD2_5:
            port = configurator.port_firebird2_5
        else:
            port = configurator.port_firebird3_0

        file_content = file_content.replace(SampleFiles.FIREBIRD_PORT, port)
        return file_content

    @staticmethod
    def write_file(content, path):
        try:
            with open(path, 'w') as file:
                file.write(content)
        except IOError:
            raise ExceptionSaveFile("Erro ao tentar escrever o arquivo!")

    @staticmethod
    def filter_list(original_list, search):
        return list(filter(lambda item: search.lower() in item.lower(), original_list))

    @staticmethod
    def format_version_database(version):
        return '{}-{}-{}-{}'.format(version[:4], version[4:6], version[6:8], version[8:])

