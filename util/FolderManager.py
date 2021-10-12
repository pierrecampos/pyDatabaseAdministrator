import os
from functools import cmp_to_key
from model.Database import Database
from util.Utils import Utils


class FolderManager:
    def __init__(self):
        pass

    @staticmethod
    def get_folders(path):
        databases = dict()
        for root, dirs, files in os.walk(path):
            for file in files:
                if str(file).lower().endswith('.fdb'):
                    name = Utils.fix_folder_name(os.path.basename(root))
                    complete_path = os.path.join(root, file)
                    databases[name] = Database(name, complete_path)
        return databases
