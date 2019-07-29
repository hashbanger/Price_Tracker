__author__ = 'hashbanger'

class Alert(object):
    def __init__(self, user, price_limit, item):
        self.user = user
        self.price_limit = price_limit
        self.item = item

    def __repr__(self):
        return "<Alert for User {} on Item {} with price {}>".format(self.user.name, self.item.name, self.price_limit)
