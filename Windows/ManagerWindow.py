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

        # Инициализация внеш. зависимостей
        self.db = db
        self.set_user = set_user
        self.get_user = get_user
        self.user = User()  # Пустой пользователь
        self.ui.logout_btn.clicked.connect(self.logout)
        self.ui.add_password_btn.clicked.connect(self.add_password)

        # Первоначальное отображение списка паролей
        # self.update_password_list()

    def clear_password_list(self):
        '''Очищает список паролей в scroll_layout'''
        while self.scroll_layout.count() > 0:  # Очистка всех элементов
            item = self.scroll_layout.itemAt(0)
            if item.widget():
                item.widget().deleteLater()
            else:
                self.scroll_layout.removeItem(item)

    def reset_scroll_area(self):
        '''Удаляет и пересоздает scroll_content_widget с новым layout'''
        # Удаляем текущий scroll_content_widget, если он существует
        if self.scroll_content_widget is not None:
            self.scroll_content_widget.deleteLater()

        # Создаем новый виджет и layout для прокрутки
        self.scroll_content_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        # Задаем новый виджет в QScrollArea
        self.ui.passArea.setWidget(self.scroll_content_widget)

    def logout(self):
        '''Выход из учётной записи'''
        self.set_user(None)
        self.clear_password_list()  # Очищаем список паролей
        self.ui.password_line.setText("")
        self.ui.service_line.setText("")
        self.stacked_widget.setCurrentIndex(0)

    def update_password_list(self):
        '''Обновляет и отображает список паролей для текущего пользователя'''
        self.reset_scroll_area()
        self.password_list = self.user.get_passwords_list(self.db)  # Получить пароли текущего пользователя
        for line in self.password_list:
            print(line)
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

            self.scroll_layout.addLayout(row_layout)

    def toggle_password_display(self, password_field):
        '''Функция, переключающая отображение пароля по нажатию'''
        if password_field.echoMode() == QLineEdit.Password:
            password_field.setEchoMode(QLineEdit.Normal)
        else:
            password_field.setEchoMode(QLineEdit.Password)

    def add_password(self):
        '''Добавляет пароль в базу данных из графического интерфейса'''
        service = self.ui.service_line.text()
        password = self.ui.password_line.text()
        self.db.add_password(self.user.get_id(), service, password)
        self.ui.password_line.setText("")
        self.ui.service_line.setText("")
        self.update_password_list()  # Обновляем список паролей после добавления

    def init_user(self):
        '''Инициализация текущего пользователя'''
        self.user = self.get_user()
        self.update_password_list()  # Обновляем список паролей при входе
