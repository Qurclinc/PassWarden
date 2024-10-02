from PyQt5.QtWidgets import QMainWindow
from src.Login import Ui_LoginWindow

class LoginWindow(QMainWindow):
    def __init__(self, stacked_widget, db):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.db = db
        self.ui.register_btn.clicked.connect(self.register_window)

    def register_window(self):
        self.stacked_widget.setCurrentIndex(1)