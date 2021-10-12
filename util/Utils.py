from PyQt5.QtWidgets import QFileDialog


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
    def fix_folder_name(name):
        return name.replace('_', ' ')
