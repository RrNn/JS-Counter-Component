from Business import Business


class User(object):

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def get_name(self):
        return 'yuppys'
