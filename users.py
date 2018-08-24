class User:
    users_list = {}

    def __init__(self, firs_name, last_name, email, password, accounts):
        self.first_name = firs_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.accounts = accounts

    def save_user(self):
        User.users_list[self.first_name + ' ' + self.last_name] = dict(
            first_name=self.first_name, last_name=self.last_name, email=self.email, password=self.password, accounts=dict())
