import webbrowser

from PyQt5.QtWidgets import QWidget, QLabel

from views.ui.InfoScreenUI import Ui_Info


class InfoScreen(QWidget, Ui_Info):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnLinkGitHub.clicked.connect(self.open_github_link)

    def open_github_link(self):
        print('ok')
        webbrowser.open(self.btnLinkGitHub.text())
