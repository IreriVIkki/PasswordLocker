class User:
    users_list = []

    def __init__(self, firs_name, last_name, email, password, accounts):
        self.firs_name = firs_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.accounts = accounts

    def save_user(self):
        User.users_list.append(self)
