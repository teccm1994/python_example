# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-04-10 08:16'


# 若实例属性和类属性有相同的名称，相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性。
class Student(object):
    # 类属性
    name = 'Student'
    # 限制实例的属性,仅对当前类有效，对继承的子类无效
    # __slots__ = ('name', 'age')

    # 数据封装
    # 通过实例变量或self变量给实例绑定属性
    # def __init__(self, name, score):
    #     self.name = name
    #     self.score = score
    #
    # def print_score(self):
    #     print('%s: %s' % (self.name, self.score))

    # 访问限制,私有变量
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_score(self):
        return self.__score

    # 对参数做检查，避免传入无效的参数
    def set_score(self, score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
if bart.get_score() != 59:
    print('test fail!')
else:
    bart.set_score(66)
    if bart.get_score() != 66:
        print('test fail!!')
    else:
        print('test success!')


# 继承和多态
class Animal(object):

    def run(self):
        print('Animal is running...')


# 继承
# 任何类最终都可以追溯到根类object
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的
class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


# 多态
# 对扩展开放：允许新增Animal子类
# 对修改封闭：不需要修改依赖Animal类型的run_twice等函数
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())


class A(object):

    def show(self):
        print('base show')


class B(A):
    def show(self):
        print('derived show')


obj = B()
obj.show()
print(dir(obj))
obj.__class__ = A
obj.show()

