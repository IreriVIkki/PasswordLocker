import string
import random
import pyperclip


class Account:

    # initialization method fo setting up an instance of class account
    def __init__(self, account_name, account_url, email, password):
        self.account_name = account_name
        self.account_url = account_url
        self.email = email
        self.password = password

    # method for saving new account details to a dict
    def save_account(self):
        account = dict(
            name=self.account_name, link_url=self.account_url, email=self.email, password=self.password)
        return account

    #  method for creating new account credentials and saving then in a dict
    def new_account(self, number):
        new_password = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=number))
        account = dict(name=self.account_name,
                       link_url=self.account_url, password=new_password)
        return account

    #  method for copying account email to the clipboard
    def copy_email(self, account, item):
        return pyperclip.copy(account[item])

    #  method for copying account password to the clipboard
    def copy_password(self, account, item):
        return pyperclip.copy(account[item])
