__author__ = 'hashbanger'

from passlib.hash import pbkdf2_sha512

class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        Hashes a password to using pbkdf2_sha512
        :param password: a sha512 hashed password from the form
        :return: a sha512 -> pbkdf2_sha512 hashed password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks whether the given password is valid or not, at this stage the
        password is hashed and not original.
        :param password: a sha512 hashed password
        :param hashed_password: a pbkdf2_sha512 hashed password
        :return: True if the passwords math, otherwise False
        """
        return pbkdf2_sha512.verify(password, hashed_password)

