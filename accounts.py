import string
import random


class Account:

    account = dict()

    def __init__(self, account_name, account_url, email, password):
        self.account_name = account_name
        self.account_url = account_url
        self.email = email
        self.password = password

    def save_account(self):
        # Account.account['name'] = self.account_name
        Account.account = dict(
            name=self.account_name, link_url=self.account_url, email=self.email, password=self.password)
        return Account.account

    def new_account(self, number):
        new_password = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=number))
        Account.account = dict(name=self.account_name,
                               link_url=self.account_url, password=new_password)
        return Account.account

    # def add_to_user():
    #     User.users_list[]
