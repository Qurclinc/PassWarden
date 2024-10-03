from PyQt5.QtWidgets import QMainWindow
from src.Manager import Ui_ManagerWindow
from Services.User import User

class ManagerWindow(QMainWindow):
    def __init__(self, stacked_widget, db, set_user, get_user):
        super(ManagerWindow, self).__init__()
        self.ui = Ui_ManagerWindow()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.db = db
        self.set_user = set_user
        self.get_user = get_user
        self.user = User()
        self.ui.logout_btn.clicked.connect(self.logout)
        self.ui.add_password_btn.clicked.connect(self.add_password)
        self.password_list = []
        self.print_list()

    def logout(self): #TODO: Дописать выход из учётки. Пока что это тестовая кнопка))
        self.set_user(None)
        self.init_user()
        self.stacked_widget.setCurrentIndex(0)

    def print_list(self): #TODO: Тяжко. Нужно написать полное отображение списка сервис + пароль текущего пользователя. Тяжко будет ui красиво сделать...
        self.password_list = self.db.get_passwords_list(self.user.get_id())
        for i in self.password_list:
            print(i)

    def add_password(self): #TODO: будущий метод для кнопки добавления пароля. пока тестовый метод.
        row_count = len(self.db.get_passwords_list(self.user.get_id()))
        self.db.add_password(self.user.get_id(), self.ui.service_line.text(), self.ui.password_line.text())
        print(row_count)
        self.print_list()

    def init_user(self):
        self.user = self.get_user()

    def update_list(self, elem=None): # универсальный метод который рассчитывает инициализацию при регистрации с возможностью добавлять новые записи. 
        # Возможно потом разделю
        self.password_list = []
        if elem:
            self.password_list += [elem]
        self.print_list()
