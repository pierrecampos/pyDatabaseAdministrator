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
    def fix_folders_name(folders):
        if folders is None:
            return

        new_folders = set()
        for folder in folders:
            folder = str(folder).replace('_', ' ')
            new_folders.add(folder)

        return new_folders
