from users import User


class Account:
    user_accounts = []

    def __init__(self, account_name, account_url, email, password):
        self.account_name = account_name
        self.account_url = account_url
        self.email = email
        self.password = password
