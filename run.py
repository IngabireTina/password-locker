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