from users import User


class Account:

    account = ()

    def __init__(self, account_name, account_url, email, password):
        self.account_name = account_name
        self.account_url = account_url
        self.email = email
        self.password = password

    def save_account(self):
        account = self.account_name, self.account_url, self.email, self.password
        # User.users_list[]
