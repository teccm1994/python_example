# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-04-21 14:43'


class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass


class Apple(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("apple is in red")


class Orange(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("orange is in orange")


class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()


fruit1 = FruitFactory("apple")
fruit2 = FruitFactory("orange")
