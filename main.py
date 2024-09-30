# from Services.Crypter import Crypter

# crypter = Crypter()
# key = "S0m3H4rdLin3"
# data = "Соси хуй чурка"
# # res = crypter.encrypt(key, data)


# encrypted_data = "HDYBF8RiUBvts/RR:DWmSNVl7+Kpt6UgLyO/O+jM+7d+XOMh8rMtRoCnIosg="

# res = crypter.decrypt(key, encrypted_data)

# print(res)

from Services.Fileworker import processing
from Services.DatabaseWorker import init_tables, Database
from Services.User import User
import bcrypt

# line = "p4$$w0rd"
# salt = bcrypt.gensalt(16)
# hash = bcrypt.hashpw(line.encode("utf-8"), salt)
# print(salt, hash, sep="\n")
# print("\n\n\n")

# newsalt = hash.decode("utf-8")[:29].encode("utf-8")
# d_line = input()
# d_hash = bcrypt.hashpw(d_line.encode("utf-8"), newsalt)
# print(newsalt, d_hash, sep="\n")
init_tables()

db = Database()

# print(db.register("Peter", "Wiener"))
# print(db.register("Bill", "N0P4$$w0rd"))
data = db.authenticate("Bill", "N0P4$$w0rd")
user = User(data[0], data[1])
# data = db.authenticate("Peter", "Wiener")
# user.add_password(db, "Менеджер паролей", "N0P4$$w0rd")
print(user.get_password(db, "Менеджер паролей"))