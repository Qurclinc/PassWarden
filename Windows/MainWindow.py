from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from .LoginWindow import LoginWindow
from .RegistrationWindow import RegisterWindow
from .ManagerWindow import ManagerWindow

class MainWindow(QMainWindow):
    def __init__(self, db):
        super(MainWindow, self).__init__()
        self.setFixedSize(640, 480)
        self.db = db
        self.user = None
        self.stacked_widget = QStackedWidget() # Стек виджетов - чтобы между окнами можно было переключаться без резких скачков
        self.register_window = RegisterWindow(self.stacked_widget, self.db)
        self.login_window = LoginWindow(self.stacked_widget, self.db, self.set_user) # Чтобы пользователь везде сохранялся и ставился правильно - передаем метод
        self.manager_window = ManagerWindow(self.stacked_widget, self.db, self.get_user) # Аналогично и для того, чтобы получать текущего пользователя

        self.stacked_widget.currentChanged.connect(self.indexChanged) # Если меняется окно - выполняется это событие и метод. Передается индекс окна на которое переключились

        # Добавление окон
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.register_window)
        self.stacked_widget.addWidget(self.manager_window)

        self.setCentralWidget(self.stacked_widget) # Так надо
        self.setWindowTitle("PassWarden")

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user
    
    def indexChanged(self, index):
        if index == 2:
            self.manager_window.update_list() # Таким образом при смене индекса окна должен обновляться список паролей и сервисов под текущего пользователя