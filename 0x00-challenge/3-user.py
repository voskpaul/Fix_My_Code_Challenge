#!/usr/bin/python3
import hashlib
import uuid

class User:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pwd):
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        if pwd is None or not isinstance(pwd, str) or self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password

if __name__ == '__main':
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "myPassword"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if set to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if set to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compared with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compared with an integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password is set before")

