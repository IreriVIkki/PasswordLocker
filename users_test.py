import unittest  # importing the unitttest module
from users import User  # importing the users class
from accounts import Account


class TestUsers (unittest.TestCase):
    # this class defines test cases for user class behaviours
    # TestCase class helps in creating testcases

    def setUp(self):
        self.new_user = User(
            'Vikki', 'Ireri', 'wambsviki@gmail.com', 'akisijui', {})
        self.new_account = Account('Instagram',  'https://www.instagram.com/',
                                   'wambsviki@gmail.com', '12345')

    def test_init(self):
        self.assertEqual(self.new_user.first_name, 'Vikki')
        self.assertEqual(self.new_user.last_name, 'Ireri')
        self.assertEqual(self.new_user.email, 'wambsviki@gmail.com')
        self.assertEqual(self.new_user.password, 'akisijui')
        self.assertEqual(self.new_user.accounts, {})

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)
        self.new_account.save_account()
        print(self.new_account)

    def test_add_account(self):
        self.new_user.add_account(self.new_account)
        # self.new_user.save_user()
        # print(self.new_user)
        # self.new_user.save_user()
        # self.new_user.add_account()


if __name__ == '__main__':
    unittest.main()
