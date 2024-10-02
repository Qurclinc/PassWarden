from PyQt5.QtWidgets import QMainWindow
from src.Manager import Ui_ManagerWindow

class ManagerWindow(QMainWindow):
    def __init__(self, stacked_widget, db, get_user):
        super(ManagerWindow, self).__init__()
        self.ui = Ui_ManagerWindow()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.db = db
        self.get_user = get_user
        self.ui.logout_btn.clicked.connect(self.logout)
        self.password_list = []

    def logout(self): #TODO: Дописать выход из учётки. Пока что это тестовая кнопка))
        user = self.get_user()
        print(user.get_id())

    def print_list(self): #TODO: Тяжко. Нужно написать полное отображение списка сервис + пароль текущего пользователя. Тяжко будет ui красиво сделать...
        for i in self.password_list:
            print(i)

    def add_password(self): #TODO: будущий метод для кнопки добавления пароля. пока тестовый метод.
        self.update_list("LOL")

    def update_list(self, elem=None): # универсальный метод который рассчитывает инициализацию при регистрации с возможностью добавлять новые записи. 
        # Возможно потом разделю
        self.password_list = ["Aboba", "Zalupa", "XD"]
        if elem:
            self.password_list += [elem]
