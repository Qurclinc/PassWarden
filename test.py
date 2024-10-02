# import base64
# from Crypto.Cipher import AES
# from Crypto import Random
# from Crypto.Util.Padding import pad, unpad
# from Services.Crypter import Crypter

# # line = input()
# line = "S0m3H4rdLin3"
# print(line, len(line))
# line = Crypter().generate_key(line)
# key = line
# iv = base64.b64encode(Random.get_random_bytes(12))
# # iv = Random.get_random_bytes(16)
# mode = AES.MODE_CBC

# encrypter = AES.new(key, mode, iv=iv)

# data = "соси хуй чурка"

# res = encrypter.encrypt(pad(data.encode("utf-8"), 16))
# enc_data = base64.b64encode(res)
# password = f"{iv.decode("utf-8")}:{enc_data.decode("utf-8")}"
# print(iv, len(iv))

# print(enc_data)
# print(password)
# print("\n\n\n")

# d_line = input()
# d_key = Crypter().generate_key(d_line)
# mode = AES.MODE_CBC
# iv, data = password.split(":")
# print(iv.encode("utf-8"), base64.b64decode(data), sep="\t")
# decrypter = AES.new(d_key, mode, iv=iv.encode("utf-8"))
# d_data = unpad(decrypter.decrypt(base64.b64decode(data)), 16)
# print(iv)
# print(d_data.decode("utf-8"))

# # from Services.Crypter import Crypter
# # crypter = Crypter()

# # x = crypter.encrypt("XUI", "иди нахуй")
# # print(x)


from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
import sys
from Login import Ui_LoginWindow
from Register import Ui_RegisterWindow

class LoginWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.register_btn.clicked.connect(self.register_window)

    def register_window(self):
        self.stacked_widget.setCurrentIndex(1)

class RegisterWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super(RegisterWindow, self).__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.setWindowTitle = "Регистрация"
        self.stacked_widget = stacked_widget
        self.ui.log_in_btn.clicked.connect(self.login_window)

    def login_window(self):
        self.stacked_widget.setCurrentIndex(0)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(640, 480)
        self.stacked_widget = QStackedWidget()
        self.login_window = LoginWindow(self.stacked_widget)
        self.register_window = RegisterWindow(self.stacked_widget)

        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.register_window)

        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle("PassWarden")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())