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

import sys

from PyQt5.QtWidgets import QApplication
from Windows.MainWindow import MainWindow

from Services.DatabaseWorker import init_tables, Database


if __name__ == "__main__":
    init_tables()
    db = Database()
    app = QApplication(sys.argv)
    main_window = MainWindow(db)
    main_window.show()
    sys.exit(app.exec())