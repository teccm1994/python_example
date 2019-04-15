# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-21 21:22'


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


@singleton
class Highlander:
    x = 100


def test():
    Highlander is Highlander() is Highlander
    id(Highlander()) == id(Highlander)
    Highlander().x == Highlander.x == 100
    Highlander.x = 50
    Highlander().x == Highlander.x == 50


test()
