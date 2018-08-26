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
        user[self.email] = dict(
            first_name=self.first_name, last_name=self.last_name, email=self.email, password=self.password, accounts=[])
        return user

    def new_credentials(self):
        pass

    def add_acc_to_user(self, account, user):
        user[self.email]['accounts'].append(account)

    def add_user_to_list(self, user):
        self.users_list.update(user)

    def delete_user_from_list(self):
        users = User.users_list
        for key, value in users.items():
            if key == self.first_name + ' ' + self.last_name:
                del users[key]
                return users

    def delete_account(self, account, user):
        list1 = user[self.email]['accounts']
        user[self.email]['accounts'] = [
            x for x in list1 if x['name'] != account]
        return user

    def find_user_by_email(self, email):
        users = User.users_list
        for key, value in users.items():
            if key == email:
                # print(value)
                return (value)

    def find_account(self):
        pass
        # print(self.accounts)


def main():
    user_options()


def user_options():
    print('OH, hi there. Im deadpool. Just kidding. You wanna login or sign up \n\n     l: to login \n      s: to signup\n ')
    choice = input().lower()

    new_user = User('', '', '', '', [])

    if choice == 's':
        f_name = input('Enter your First Name:___')
        l_name = input('Enter your Last Name:___')
        email = input('Enter your Email:___')
        password = input('Enter your Password:___')
        c_password = input('Confirm your Password:___')
        full_name = f'{f_name} {l_name}'

        if password == c_password:
            new_user = User(f_name, l_name, email, password, [])
            user_acc = new_user.save_user()
            new_user.add_user_to_list(user_acc)

            print('\n\nCongrats! your account has been created successfully.\n\n')

            print('What would you like to do now?\n\n')

            print(User.users_list)

            account_options(new_user, user_acc, full_name)

    if choice == 'l':
        user_email = input('Enter your email:___')
        user_password = input('Enter your password:___')

        user_acc = new_user.find_user_by_email(user_email)

        if user_acc['password'] == user_password:
            print(user_acc)

            account_options(new_user, user_acc, full_name)


def account_options(new_user, user_acc, full_name):

    print('s: save an existing account\nc: create a new account\nd: delete an account\nx: log out from your account\n')

    option = input('Enter your choice here:___')

    if option == 's':
        ac_name = input('Enter account name:___')
        ac_url = input('Enter account url:___')
        ac_email = input('Enter account email:___')
        ac_password = input('Enter account password:___')

        new_acc = Account(ac_name, ac_url, ac_email,
                          ac_password).save_account()

        new_user.add_acc_to_user(new_acc, user_acc)

        print('\n\nWhat else would you like to do?\n')

        account_options(new_user, user_acc, full_name)

        print('\n\n')

    elif option == 'c':
        cac_name = input('Enter account name:___')
        cac_url = input('Enter account url:___')
        cac_email = input('Enter account email:___')
        cac_pass_length = int(input('Enter length of password'))

        new_acc = Account(cac_name, cac_url,
                          cac_email, '').new_account(cac_pass_length)

        new_user.add_acc_to_user(new_acc, user_acc)

        print(
            f'Your new login credentials are:\n\nEmail:  {new_acc["name"]}\npassword  {new_acc["password"]}')
        print('\n\nWhat else would you like to do?\n')

        account_options(new_user, user_acc, full_name)

        print('\n\n')

    elif option == 'd':
        name_delete = input('Enter name of account to delete:___')
        new_user.delete_account(name_delete, user_acc)

        print('\n\nWhat else would you like to do?\n')

        account_options(new_user, user_acc, full_name)

    elif option == 'x':
        print('You have logged out of your account')

        print('\n\nWhat else would you like to do?\n\n')
        user_options()
        print('\n\n')
        pass


if __name__ == '__main__':
    main()
