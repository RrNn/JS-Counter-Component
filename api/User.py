from Business import Business


class User(object):
    user = {
        'name': 'Nabaasa Richard',
        'email': 'nabaasarichard@gmail.com',
        'password': 'passwrd'
    }
    logged_in = False

    def __init__(self):
        pass

    def register(self, name, email, password):
        self.user['name'] = name
        self.user['email'] = email
        self.user['password'] = password

    def login(self):
        self.logged_in = True
        return 'You are logged in'

    def logout(self):
        self.logged_in = False
        return 'You are now logged out'

    def reset_pass(self, new_password):
        self.user['password'] = new_password

    def get_name(self):
        return self.user
