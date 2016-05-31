class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True


class Token():
    def __init__(self, token, expire, user):
        self.token = token
        self.expire = expire
        self.user = user       
