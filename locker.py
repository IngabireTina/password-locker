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

class Credential():

    # Creation of credential class and will help to create new credentials
    credentials = []

    def __init__(self, account_name, user_name, account_password):
     #class instance
        self.account_name - account_name
        self.user_name = user_name
        self.account_password = account_password

    @classmethod
    def user_checker(cls. username, password):
        #does user exist?

        for user in User.users:
            if(user.username == username and user.password == password):
                user == user.username
            return user

    def save_credential(self):
        #save the credential
        Credential.credentials.append(self)

    def delete_credential(self):
        # delete credential method
            Credential.credentials.remove(self)


 
