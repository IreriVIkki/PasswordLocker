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


def main():
    print('Oh, hi there, I\'m Deadpool!!. lets create a lastpass account for you. \n What is your name? \n ')
    user_name = input()

    print(f'So, {user_name} what would you like to do?')

    print('use the following short-codes \n new-acc ---> to sign up \n login ---> to login to your account \n new-site ---> to add a new site credentials \n new-cred ---> to generate new credentials')

    choice = input().lower()

    if choice == 'new-acc':
        first_name = input('Enter your first name:__')
        last_name = input('Enter your last name:__')
        email = input('Enter your email:__')
        password = input('Enter your new password:__')
        v_password = input('Confirm your new password:__')

        if password == v_password:
            new_user_acc = User(first_name, last_name, email, password, [])
            new_user_acc.save_user()

            print(f'your account {new_user_acc.first_name} has been created')

            print(new_user_acc.save_user())


if __name__ == '__main__':
    main()
