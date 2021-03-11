import random

class User: 
    # created class user

    users = []

    def __init__(self,username,password):

        #generated new instance of user

        self.username = username
        self.password = password

    def save_user(self):
        # function to create user credentials

        User.users.append(self)
    @classmethod
    def list_users(cls):
        #method to display credentials
        return cls.users

    def delete(cls):
        #method to delete credentials
        User.users.remove(self)
        