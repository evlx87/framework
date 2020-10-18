"""Функционал логирования событий"""

import time
from base.patterns import SingletonByName


class Logger(metaclass=SingletonByName):
    def __init__(self, name):
        self.name = name

    def log(self, text):
        print('LOG---->\t', text)


def debug(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('DEBUG-->\t', func.__name__, end - start)
        return result
    return inner
