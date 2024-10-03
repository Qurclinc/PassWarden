from PyQt5.QtWidgets import QMainWindow
from src.Login import Ui_LoginWindow
from Services.User import User

class LoginWindow(QMainWindow):
    def __init__(self, stacked_widget, db, set_user):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.db = db
        self.set_user = set_user # инициализируем тот метод чтобы выставить пользователя 
        self.ui.register_btn.clicked.connect(self.register_window)
        self.ui.log_in_btn.clicked.connect(self.log_in)

    def reset(self):
        self.ui.line_login.setText("")
        self.ui.line_password.setText("")

    def register_window(self):
        self.stacked_widget.setCurrentIndex(1)

    def log_in(self): # TODO: авторизация не доделана; нужно дописать обработку ошибок авторизации. 
        login = self.ui.line_login.text()
        password = self.ui.line_password.text()
        res = self.db.authenticate(login, password)
        # if res: print(res)
        # else: print("Error")
        self.set_user(User(res[0], res[1])) # Установка пользователя
        self.stacked_widget.setCurrentIndex(2) # Смена окна