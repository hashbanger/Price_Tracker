__author__ = ' hashbanger'

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors
import uuid


class User(object):
    def __init__(self, email, password, _id = None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This checks if the email-password combo passed by the user is valid or not.
        :param email: the email id of the user to check
        :param password: a sha512 hashed password of the user
        :return: True if the id is valid else False
        """
        user_data = Database.find_one('users', query = {'email': email})
        if user_data is None:
            # Tell the user that email does not exists
            raise UserErrors.UserNotExistsError('The user does not exists.')

        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell the user that password is wrong
            raise UserErrors.IncorrectPasswordError('The password provided is wrong')

        return True


