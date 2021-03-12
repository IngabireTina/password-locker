#!/usr/bin/env python3.6
from locker import User, Credential


 #method to create user
def create_user(username, password):

    user = User(username, password)
    return user

#method to save user
def save_user(user):
  
    user.save_user()

#display all users
def list_users():
    return User.list_users()

#method to check if user exist
def user_checker(username,password):
    user_checker = Credential.user_checker(username,password)
    return user_checker




#create new account credential
def create_credential(username,password,account_name):
   
    credential = Credential(username,password,account_name)
    return credential


#saving credential
def save_credential(credential):
    credential.save_credential()


#delet account credential
def delete_credential(credential):
    credential.delete_credential()

# search the account credential
def search_credential(credential):
    return Credential.search_credential(credential)


# view all the account credentials
def view_all_credential():
    return Credential.view_all_credential()
