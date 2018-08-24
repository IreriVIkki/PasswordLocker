import unittest  # importing the unitttest module
from users import User  # importing the users class
from accounts import Account


class TestUsers (unittest.TestCase):
    # this class defines test cases for user class behaviours
    # TestCase class helps in creating testcases

    def setUp(self):
        self.new_user = User(
            'Vikki', 'Ireri', 'wambsviki@gmail.com', 'akisijui', [])
        self.new_account = Account('Instagram',  'https://www.instagram.com/',
                                   'wambsviki@gmail.com', '12345')
        self.new_account1 = Account('Facebook',  'https://www.facebook.com/',
                                    'wambsviki@gmail.com', '67890')

    def test_init(self):
        self.assertEqual(self.new_user.first_name, 'Vikki')
        self.assertEqual(self.new_user.last_name, 'Ireri')
        self.assertEqual(self.new_user.email, 'wambsviki@gmail.com')
        self.assertEqual(self.new_user.password, 'akisijui')
        self.assertEqual(self.new_user.accounts, [])

    # def test_save_user(self):
    #     self.new_user.save_user()
        # self.new_account.save_account()

    def test_add_to_user(self):
        user = self.new_user.save_user()
        acc1 = self.new_account1.save_account()
        acc = self.new_account.save_account()
        self.new_user.add_to_user(acc1, user)
        self.new_user.add_to_user(acc, user)
        self.assertEqual(len(user['Vikki Ireri']['accounts']), 2)
        print(user)


if __name__ == '__main__':
    unittest.main()
