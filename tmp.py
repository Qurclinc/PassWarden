from Services.User import User
from Services.DatabaseWorker import Database

db = Database()
res = db.authenticate("Peter", "Wiener123")
res = db.authenticate("Bill", "754015Qwe")
user = User(res[0], res[1])
print(user.get_passwords_list(db))