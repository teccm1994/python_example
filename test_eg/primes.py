# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-21 20:15'

import unittest


def is_prime(number):
    """
    判断一个数是否是素数（一个比1大并且只能被1和它本身整除的数）
    return True if number is prime
    """
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def print_next_prime(number):
    """
    Print the closest prime number larger than number.
    """
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)


class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        self.assertFalse(is_prime(4), msg="Four is not prime!")

    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))


if __name__ == '__main__':
    unittest.main()
