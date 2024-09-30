class User:

    def __init__(self, id, login):
        self.id = id
        self.login = login

    def get_id(self):
        return self.id
    
    def get_login(self):
        return self.login
    
    def add_password(self, db, service, password):
        db.add_password(self.get_id(), service, password)

    def get_password(self, db, service):
        return db.get_password(self.get_id(), service)
    
    def get_passwords_list(self, db):
        return db.get_passwords_list(self.id)

