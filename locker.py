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
