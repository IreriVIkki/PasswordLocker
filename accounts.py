import string
import random


class Account:

    def __init__(self, account_name, account_url, email, password):
        self.account_name = account_name
        self.account_url = account_url
        self.email = email
        self.password = password

    def save_account(self):
        account = dict(
            name=self.account_name, link_url=self.account_url, email=self.email, password=self.password)
        return account

    def new_account(self, number):
        new_password = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=number))
        account = dict(name=self.account_name,
                       link_url=self.account_url, password=new_password)
        return account
