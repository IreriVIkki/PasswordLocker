class Account:

    account = dict()

    def __init__(self, account_name, account_url, email, password):
        self.account_name = account_name
        self.account_url = account_url
        self.email = email
        self.password = password

    def save_account(self):
        Account.account['name'] = self.account_name
        Account.account['details'] = dict(
            name=self.account_name, link_url=self.account_url, email=self.email, password=self.password)

    # def add_to_user():
    #     User.users_list[]
