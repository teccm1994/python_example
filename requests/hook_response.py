# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-17 15:00'

import requests


def get_key_info(response, *args, **kwargs):
    """
    回调函数
    :param response:
    :param args:
    :param kwargs:
    :return:
    """
    print(response.headers['Content-Type'])


def main():
    """
    主函数
    :return:
    """
    requests.get('https://www.baidu.com', hooks=dict(response=get_key_info))


main()
