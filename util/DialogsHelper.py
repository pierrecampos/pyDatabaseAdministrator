from PyQt5.QtWidgets import QMessageBox


class DialogsHelper:

    @staticmethod
    def show_info(parent=None, title='Informação', message='Informação'):
        QMessageBox.information(parent, title, message)

    @staticmethod
    def show_warning(parent=None, title='Atenção', message='Atenção'):
        QMessageBox.warning(parent, title, message)

    @staticmethod
    def show_error(parent=None, title='Atenção', message='Atenção'):
        QMessageBox.critical(parent, title, message)