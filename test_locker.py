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

if __name__ == '__main__':
    unittest.main()
        