import unittest  # importing the unitttest module
from users import User  # importing the users class


class TestUsers (unittest.TestCase):
    # this class defines test cases for user class behaviours
    # TestCase class helps in creating testcases

    def setUp(self):
        self.new_user = User(
            'Victor', 'Ireri', 'wambsviki@gmail.com', 'akisijui', [])

    def test_init(self):
        self.assertEqual(self.new_user.firs_name, 'Victor')
        self.assertEqual(self.new_user.last_name, 'Ireri')
        self.assertEqual(self.new_user.email, 'wambsviki@gmail.com')
        self.assertEqual(self.new_user.password, 'akisijui')
        self.assertEqual(self.new_user.accounts, [])
