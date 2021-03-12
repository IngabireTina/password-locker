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

# get random password
def generate_password():
    password = Credential.generate_password()
    return password

# check if credential are true
def creadential_checker(credential):
    return Credential.creadential_checker(credential)

def main():
    print('&'*25)
    print("\t PASSWORD LOCKER")  
    print('&'*25)
    print('\n')
    print(''*20)
    print("Enter the one of the following letter to continue:\n c ---------- Create an account \n l ---------- Login if you already have an account \n")
    print('@'*20)
    abbreviation = input().lower()
    print('@'*20)
    if abbreviation == 'c':
        print('@'*20)
        print("Create an account in PASSWORD LOCKER")
        print('@'*20)
        username = input('Username: ')
        while True:
            print('@'*20)
            print('Enter the following to continue: \n p ---------- Type a password\n g ---------- generate a password fro you\n')
            print('@'*20)
            abbreviation = input().lower()
            if abbreviation == 'p':
                password = input("Enter a password for your account\n")
                break
            elif abbreviation == 'g':
                password = generate_password()
                break
            else:
                print('@'*20)
                print('Invalid password')
                print('@'*20)
            
        save_user(create_user(username,password))
        print('@'*20)
        print(f"Created an Account with username {username} and password {password}")
        print('@'*20)
    
    elif abbreviation == 'l':
        print('@'*20)
        print("Enter your user name and your password to continue")
        print('@'*20)
        username = input("Username: ")
        password = input("password: ")
        login = user_checker(username,password)
        if user_checker == login:
            print('@'*20)
            print(f"Hello {username}.Welcome To PASSWORD LOCKER \n")  
            print('@'*20)
    
    while True:
        print('@'*20)
        print("Enter the following to continue: \n c ---------- Create a new account credential \n lc ---------- Display all acount credentials \n sc ---------- Search for an account credential \n g ---------- To generate password for you \n d ---------- Delete credential \n e ---------- To Exit  \n")
        print('@'*20)
        abbreviation = input().lower()
        if abbreviation == "c":
            print('@'*20)
            print("Create new account credential")
            print("@"*20)
            print("Account name ....")
            account_name = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print('@'*20)
                print("Enter the following to continue: \n p ---------- To type your own pasword if you have an account:\n g - To generate Password for you")
                print('@'*20)
                password = input().lower()
                if password== 'p':
                    password = input("Enter Password\n")
                    break
                elif password == 'g':
                    password = generate_password()
                    break
                else:
                    print('@'*20)
                    print("Invalid password please try again")
                    print('@'*20)
            save_credential(create_credential(account_name,username,password))
            print('@'*20)
            print(f"Created an Account credential for  {account_name} with a username of {username} and password {password}")
            print('@'*20)

        elif abbreviation == "lc":
            if view_all_credential():
                print('@'*20)
                print("Your saved credentials accounts: ")
                print('@'*20)
                for account in view_all_credential():
                    print('@'*20)
                    print(f"+ Account:{account.account_name} \n User Name:{username}\n Password:{password}")
                    print('@'*20)
                print('@' * 20)
            else:
                print('@'*20)
                print("You don't have any credentials account yet!!")
                print('@'*20)

        elif abbreviation == "sc":
            print('@'*20)
            print("Enter account name ")
            print('@'*20)
            search= input().lower()
            if search_credential(search):
                credential_ = search_credential(search)
                print('@'*20)
                print(f"Account Name : {credential_.account_name}")
                print('~' * 10)
                print(f"User Name: {credential_.user_name} Password :{credential_.account_password}")
                print('~' * 10)
                print('@'*20)
            else:
                print('@'*20)
                print("Credential does not exist\n")
                print('@'*20)

        elif abbreviation == "d":
            print('@'*20)
            print("Enter the account name  you want to delete")
            print('@'*20)
            search = input().lower()
            if search_credential(search):
                credential = search_credential(search)
                print("~"*10)
                credential.delete_credential()
                print('\n')
                print(f"{credential.account_name} deleted!!!")
                print('\n')
            else:
                print("Credential does not exist ")
        
        elif abbreviation == 'g':
            password = generate_password()
            print(f" {password} password generated succesfull.")
        elif abbreviation == 'e':
            print("Bye Nice Time!!")
            break
        else:
            print("Try again")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()
