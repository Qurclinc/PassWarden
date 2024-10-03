from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from src.Manager import Ui_ManagerWindow
from Services.User import User

class ManagerWindow(QMainWindow):
    def __init__(self, stacked_widget, db, set_user, get_user):
        super(ManagerWindow, self).__init__()
        self.ui = Ui_ManagerWindow()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget

        self.scroll_content_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content_widget)  # Лейаут для области прокрутки

        # Устанавливаем виджет с лейаутом в passArea
        self.ui.passArea.setWidget(self.scroll_content_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        # Инициализация внеш. зависимостей: подтягивается база данных из точки запуска, главная и единственная, а также методы для авторизации пользователей
        self.db = db
        self.set_user = set_user
        self.get_user = get_user
        self.user = User() # пустой пользователь, так надо.
        self.ui.logout_btn.clicked.connect(self.logout)
        self.ui.add_password_btn.clicked.connect(self.add_password)
        self.password_list = []
        self.row_count = len(self.user.get_passwords_list(self.db))
        self.print_list()

    def clear_password_list(self):
        '''Очищает список паролей в scroll_layout'''
        for i in reversed(range(self.scroll_layout.count())):  # Очистка
            item = self.scroll_layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

    def logout(self):
        '''Выход из учётной записи'''
        self.set_user(None)
        # self.init_user()
        self.ui.password_line.setText("")
        self.ui.service_line.setText("")
        self.clear_password_list()
        self.stacked_widget.setCurrentIndex(0)


    def print_list(self): #TODO: Тяжко. Нужно написать полное отображение списка сервис + пароль текущего пользователя. Тяжко будет ui красиво сделать...
        self.clear_password_list()
        self.password_list = self.user.get_passwords_list(self.db)
        for line in self.password_list:
            service = line[2]
            password = self.user.get_password(self.db, service)

            row_layout = QHBoxLayout()

            service_label = QLabel(service)
            row_layout.addWidget(service_label)

            password_field = QLineEdit()
            password_field.setEchoMode(QLineEdit.Password)
            password_field.setText(password)
            password_field.setReadOnly(True)
            row_layout.addWidget(password_field)

            show_password_btn = QPushButton("👁")
            show_password_btn.clicked.connect(lambda _, p=password_field: self.toggle_password_display(p))
            row_layout.addWidget(show_password_btn)

            # self.ui.verticalLayout.addLayout(row_layout)
            self.scroll_layout.addLayout(row_layout)


    def toggle_password_display(self, password_field):
        '''Функция, переключающая отображение парооля по нажатию'''
        if password_field.echoMode() == QLineEdit.Password:
            password_field.setEchoMode(QLineEdit.Normal)
        else:
            password_field.setEchoMode(QLineEdit.Password)


    def add_password(self):
        '''Добавляет пароль в базу данных из графического интерфейса'''
        print("list:", self.user.get_passwords_list(self.db))
        self.row_count = len(self.user.get_passwords_list(self.db))
        self.db.add_password(self.user.get_id(), self.ui.service_line.text(), self.ui.password_line.text())
        print(self.row_count)
        self.ui.password_line.setText("")
        self.ui.service_line.setText("")
        self.print_list()


    def init_user(self):
        self.user = self.get_user()