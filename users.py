from accounts import Account


class User():

    users_list = {}

    def __init__(self, first_name, last_name, email, password, accounts):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.accounts = []

    def save_user(self):
        user = {}
        user[self.first_name + ' ' + self.last_name] = dict(
            first_name=self.first_name, last_name=self.last_name, email=self.email, password=self.password, accounts=[])
        return user

    def add_to_user(self, account, user):
        name = self.first_name + ' ' + self.last_name
        user[name]['accounts'].append(account)

    def add_user_to_list(self, user):
        self.users_list.update(user)

    def delete_user_from_list(self):
        users = User.users_list
        for key, value in users.items():
            if key == self.first_name + ' ' + self.last_name:
                del users[key]
                return users

    # def delete_account(self, account, user):
    #     name = self.first_name + ' ' + self.last_name
    #     list1 = user[name]['accounts']
    #     user[name]['accounts'] = [x for x in list1 if x['name'] != account]
    #     return user
