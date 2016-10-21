# coding=utf-8


class EmailExist(Exception):
    pass


class PasswordError(Exception):
    pass


class UserNotExist(Exception):
    pass


class UserHasActivated(Exception):
    pass
