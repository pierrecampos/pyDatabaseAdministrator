import inspect
import os

from PyQt5.QtCore import QDir

from model.Database import Database


class FolderManager:
    def __init__(self):
        pass

    @staticmethod
    def get_folders(path):
        databases = dict()
        for root, dirs, files in os.walk(path):
            for file in files:
                if str(file).lower().endswith('.fdb'):
                    name = FolderManager.fix_folder_name(os.path.basename(root))
                    complete_path = os.path.join(root, file)
                    databases[name] = Database(name, complete_path)
        return databases

    @staticmethod
    def fix_folder_name(name):
        return name.replace('_', ' ')

    @staticmethod
    def fix_path(path):
        return os.path.abspath(path)

    @staticmethod
    def get_full_path(suffix_path):
        return os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe()))) + QDir.separator() + suffix_path
