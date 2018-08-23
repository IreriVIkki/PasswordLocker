import unittest
from users import User
from accounts import Account


class AccountsTest(unittest.TestCase):

    def setUp(self):
        self.new_account = Account(
            'Instagram', 'https://www.instagram.com/', 'wambsviki@gmail.com', '12345')

    def test_init(self):
        self.assertEqual(self.new_account.account_name, 'Instagram')
        self.assertEqual(self.new_account.account_url,
                         'https://www.instagram.com/')
        self.assertEqual(self.new_account.email, 'wambsviki@gmail.com')
        self.assertEqual(self.new_account.paa, '12345')
