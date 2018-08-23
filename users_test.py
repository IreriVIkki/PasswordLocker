import unittest  # importing the unitttest module
from users import User  # importing the users class


class TestUsers (unittest.TestCase):
    # this class defines test cases for user class behaviours
    # TestCase class helps in creating testcases

    def setUp(self):
        self.new_user = User(
            'Victor', 'Ireri', 'wambsviki@gmail.com', 'akisijui', [])
