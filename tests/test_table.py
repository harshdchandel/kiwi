# -*- coding: utf-8 -*-

from kiwi import *


def test_basic():
    class User(Table):
        __tablename__ = 'user'

        id = HashKeyField()

