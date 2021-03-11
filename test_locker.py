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


    def save_credential_test(self):

        #is credential saved successful?
        self.credential.save_credential()
        self.assertEqual(len(Credential.credentials),1)


    def tearDown(self):

        # method after each test done
        Credential.credentials = []

    def test_save_multiple_accounts(self):

        #test to check if saving many credentials is working
        self.credential.save_credential()
        test_credential = Credential("instagram","clementine","tine") 
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials),2)


    def test_deleted_credential(self):
        # check if u can delete account credential

        self.credential.save_credential()
        test_credential = Credential("instagram","clementine","tine") 
        test_credential.save_credential()
        self.credential.delete_credential()
        self.assertEqual(len(Credential.credentials),1) 

    def test_search_credential(self):
        
         #can u find account credential(searching)
        self.credential.save_credential()
        test_credential = Credential("instagram","clementine","tine")  
        test_credential.save_credential()
        found = Credential.search_credential("instagram")
        self.assertEqual(found.account_name,test_credential.account_name)

    def test_credential(self):

        #does the credential account exist?

        self.credential.save_credential()
        found = Credential("instagram","clementine","tine")  
        found.save_credential()
        credential_found = Credential.search_credential("Istagram")
        self.assertTrue(credential_found)






if __name__ == '__main__':
    unittest.main()
        