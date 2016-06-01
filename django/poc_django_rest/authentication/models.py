# -*- coding: utf-8 -*-
class User():
    def __init__(self, id, username, password, first_name, last_name, email):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def is_authenticated(self):
        return True


class Token():
    def __init__(self, token, expires, user):
        self.token = token
        self.expires = expires
        self.user = user       