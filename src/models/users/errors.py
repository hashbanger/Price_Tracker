__author__ = 'hashbanger'

class UserError(object):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserError):
    pass

class IncorrectPasswordError(object):
    def __init__(self, message):
        self.message = message
