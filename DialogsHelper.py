from PyQt5.QtWidgets import QMessageBox


class DialogsHelper:

    @staticmethod
    def show_info(parent=None, title='Informação', message='Informação'):
        QMessageBox.information(parent, title, message)
