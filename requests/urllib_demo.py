# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-15 08:32'

import urllib
import urllib2

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET= 'http://127.0.0.1:8000/get'


def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print('>>>>Response Headers:')
    print(response.info())
    print('>>>>Response Body:')
    print(''.join([line for line in response.readlines()]))


def use_params_urllib2():
    params = urllib.urlencode({'param1': 'hello', 'param2': 'word'})
    print('Request Params:')
    print(params)
    response = urllib2.urlopen('?'.join([URL_GET, '%s']) % params)
    print('>>>>Response Headers:')
    print(response.info())
    print('>>>>Status Code:')
    print(response.getcode())
    print('>>>>Response Body:')
    print(''.join([line for line in response.readlines()]))


if __name__ == '__main__':
    print('>>>Use simple urllib2:')
    use_simple_urllib2()
    print('')
    print('>>>Use params urllib2:')
    use_params_urllib2()
