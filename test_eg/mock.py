# -*- coding:utf-8 -*-
# mock is a library for testing in Python.
# https://docs.python.org/dev/library/unittest.mock.html
# https://github.com/testing-cabal/mock
__author__ = 'chen_ming'
__date__ = '2019-03-20 08:22'

import logging
from unittest.mock import Mock
from unittest.mock import MagicMock

logging.basicConfig(level=logging.DEBUG)


class ASpecificException(Exception):
    pass


def foo():
    pass


def bar():
    try:
        logging.info("enter function <foo> now")
        foo()
    except ASpecificException:
        logging.exception("we caught a specific exception")


def test_foo():
    foo = Mock(side_effct=ASpecificException())
    logging.info("enter function <bar> now")
    bar()
    logging.info("everything just be fine")


class ProductionClass():
    pass


def test_magic():
    thing = ProductionClass()
    thing.method = MagicMock(return_value=3)
    thing.method(3, 4, 5, key='value')
    thing.method.assert_called_with(3, 4, 5, key='value')


test_foo()

