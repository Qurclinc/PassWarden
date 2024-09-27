import sqlite3 as sql
from Services.Fileworker import processing
import bcrypt
from Services.Crypter import Crypter

def init_tables():
    if processing("first_run", "false") == "true":
        with sql.connect(processing("db_location")) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
id integer PRIMARY KEY AUTOINCREMENT,
login text NOT NULL,
password text NOT NULL
);""")
            cur.execute("""CREATE TABLE IF NOT EXISTS passwords(
id integer PRIMARY KEY AUTOINCREMENT,
owner_id integer NOT NULL,
service text NOT NULL,
password text NOT NULL,
FOREIGN KEY (owner_id) REFERENCES users (id)
);""")
            conn.commit()

class Database:

    def __init__(self):
        self.route = processing("db_location")
        self.SALT_LENGTH = 29
        self.__key = None

    def get_key(self):
        if self.__key: return self.__key

    def get_user(self, id):
        try:
            with sql.connect(self.route) as conn:
                cur = conn.cursor()
                cur.execute("""SELECT * FROM users WHERE id=?""", (id,))
                res = cur.fetchone()
                if res: return res
                return []
        except Exception as ex:
            return str(ex)

    def register(self, login, password):
        try:
            salt = bcrypt.gensalt(16)
            hash = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
            with sql.connect(self.route) as conn:
                cur = conn.cursor()
                cur.execute("""SELECT COUNT() as 'count' FROM users WHERE login=?""", (login,))
                count = cur.fetchone()[0]
                if count == 0:
                    cur.execute("""INSERT INTO users(login, password) VALUES (?, ?)""", (login, hash))
                    conn.commit()
                    return True
                return False
        except sql.Error as ex:
            return str(ex)

    def authenticate(self, login, password):
        try:
            with sql.connect(self.route) as conn:
                cur = conn.cursor()
                cur.execute("""SELECT password FROM users WHERE login=?""", (login,))
                db_passwd = cur.fetchone()[0]
                salt = db_passwd[:self.SALT_LENGTH]
                hash = bcrypt.hashpw(password.encode("utf-8"), salt.encode("utf-8")).decode("utf-8")
                if hash == db_passwd:
                    cur.execute("""SELECT * FROM users WHERE login=?""", (login,))
                    self.__key = password
                    res = cur.fetchall()[0]
                    if res: return res
        except TypeError:
            return "You aren't authorized"
        except Exception as ex:
            return str(ex)

        
    def add_password(self, id, service, password):
        crypter = Crypter()
        try:
            if self.__key:
                hashed_password = crypter.encrypt(self.__key, password)
            else:
                raise BaseException("Unauthorized")
        except Exception as ex:
            return str(ex)
        try:
            with sql.connect(self.route) as conn:
                cur = conn.cursor()
                cur.execute("""INSERT INTO passwords (owner_id, service, password) VALUES (?, ?, ?)""", (id, service, hashed_password))
                conn.commit()
        except Exception as ex:
            return str(ex)
        
    def get_password(self, id, service):
        try:
            with sql.connect(self.route) as conn:
                cur = conn.cursor()
                cur.execute("""SELECT * FROM users WHERE id=? AND service=?""", (id, service))
                res = cur.fetchall()
                print(res)
        except Exception as ex:
            print(str(ex))
