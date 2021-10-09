import os

from util.Utils import Utils


class FolderManager:
    def __init__(self):
        pass

    @staticmethod
    def get_folders(path):
        folders = set()
        for root, dirs, files in os.walk(path):
            for file in files:
                if str(file).endswith('.fdb'):
                    folders.add(os.path.basename(root))
        folders = Utils.fix_folders_name(folders)
        return sorted(folders)
