import unittest
from locker import User, Credential

class User_Test(unittest.TestCase):

# to test user class
    def setUp(self):

        #function that runs before
        self.user = User('ingabire','ingabire')

    def test_init(self):

        #is user created correctly
        self.assertEqual(self.user.username,'ingabire')
        self.assertEqual(self.user.password,'ingabire')


    def test_save_user(self):

        # is the user saved
        self.user.save_user()
        self.assertEqual(len(User.users),1)



class Credential_Test(unittest.TestCase):
    def setUp(self):
        #function that runs before
        self.credential = Credential('instagram','ingabire','ingabire')

    # to check if the crediantial was correctly created
    def test_init(self):
        self.assertEqual(self.credential.account_name,'instagram')
        self.assertEqual(self.credential.user_name,'ingabire')
        self.assertEqual(self.credential.account_password,'ingabire')

if __name__ == '__main__':
    unittest.main()
        