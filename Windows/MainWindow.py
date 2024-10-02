from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from .LoginWindow import LoginWindow
from .RegistrationWindow import RegisterWindow

class MainWindow(QMainWindow):
    def __init__(self, db):
        super(MainWindow, self).__init__()
        self.setFixedSize(640, 480)
        self.db = db
        self.stacked_widget = QStackedWidget()
        self.login_window = LoginWindow(self.stacked_widget, self.db)
        self.register_window = RegisterWindow(self.stacked_widget, self.db)

        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.register_window)

        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle("PassWarden")