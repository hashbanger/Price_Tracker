__author__ = 'hashbanger'

class UserNotExistsError(object):
    def __init__(self, message):
        self.message = message

class IncorrectPasswordError(object):
    def __init__(self, message):
        self.message = message
