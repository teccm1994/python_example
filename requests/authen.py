# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-17 15:08'

import requests
import base64

BASE_URL = 'https://api.github.com'


def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])


def basic_auth():
    """
    基本认证(username, password)
    :return:
    """
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print(response.text)
    print(response.request.headers)

    basic = base64.b64decode('aW1vb2NkZW1vOmltb29jZGVtbzEyMw==')
    print(basic)


def basic_oauth():
    """
    OAUTH认证
    :return:
    """
    headers = {'Authorization': 'token dd6322fa6c57a548268453dc245cbcdc352a7811'}
    response = requests.get(construct_url('user/emails'), headers=headers)
    print(response.request.headers)
    print(response.text)
    print(response.status_code)
    print(response.reason)


from requests.auth import AuthBase


class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r


def oauth_advanced():
    auth = GithubAuth('dd6322fa6c57a548268453dc245cbcdc352a7811')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print(response.status_code)
    print(response.text)


def proxy_test():
    proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}
    url = 'https://www.facebook.com'
    response = requests.get(url, timeout=10, proxies=proxies)
    print(response.status_code)


oauth_advanced()

