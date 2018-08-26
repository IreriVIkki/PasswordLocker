#!/usr/bin/env python3.6
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

    def new_credentials(self):
        pass

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

    def delete_account(self, account, user):
        name = self.first_name + ' ' + self.last_name
        list1 = user[name]['accounts']
        user[name]['accounts'] = [x for x in list1 if x['name'] != account]
        return user

    def find_user(self, name):
        users = User.users_list
        for key, value in users.items():
            if key == name:
                # print(value)
                return (value)

    def find_account(self):
        pass
        # print(self.accounts)


def main():
    print('OH, hi there. Im deadpool. Just kidding. You wanna login or sign up \n\n     l: to login \n      s: to signup\n ')
    choice = input().lower()

    if choice == 'l':
        input('Enter your email:___')
        input('Enter your password:___')

    elif choice == 's':
        f_name = input('Enter your First Name:___')
        l_name = input('Enter your Last Name:___')
        email = input('Enter your Email:___')
        password = input('Enter your Password:___')
        c_password = input('Confirm your Password:___')

        if password == c_password:
            user_acc = User(f_name, l_name, email, password, []).save_user()


if __name__ == '__main__':
    main()
