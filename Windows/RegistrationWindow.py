from PyQt5.QtWidgets import QMainWindow, QMessageBox, QStyle, QApplication
from src.Register import Ui_RegisterWindow
from .CriticalWindow import CriticalWindow
from .SuccessWindow import SuccessWindow

from Services.Security import validate_password

class RegisterWindow(QMainWindow):
    def __init__(self, stacked_widget, db):
        super(RegisterWindow, self).__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.db = db
        self.ui.log_in_btn.clicked.connect(self.login_window)
        self.ui.register_btn.clicked.connect(self.register)

    def login_window(self):
        self.stacked_widget.setCurrentIndex(0)

    def register(self):
        login = self.ui.login_line.text()
        passwd = self.ui.passwd_line.text()
        passwd2 = self.ui.passwd2_line.text()
        if passwd == passwd2:
            res = validate_password(passwd)
            if res[0]:
                if (self.db.register(login, passwd)):
                    success_win = SuccessWindow("Успешная регистрация", "Регистрация прошла успешно. Теперь можно произвести вход в созданный аккаунт")
                    success_win.exec_()
                else:
                    error_win = CriticalWindow("Ошибка регистрации", "Имя пользователя уже занято").exec_()
            else:
                error_win = CriticalWindow(res[1], res[2])
                error_win.exec_()
        else:
            error_win = CriticalWindow("Ошибка регистрации", "Пароли не совпадают")
            error_win.exec_()
            
            