# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-17 09:27'

import json
import requests
from requests import exceptions

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    # response = requests.get(build_uri('users/imoocdemo'))
    response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'))
    print(better_print(response.text))


def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)



def json_request():
    # response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'), json={'name': 'bodymooc2', 'email': 'hello-world@imooc.org'})
    response = requests.post(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'),
                             json=['helloword@github.com'])
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)


def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), timeout=2)
    except exceptions.Timeout as e:
        print(e.message)
    else:
        print(better_print(response.text))


def hard_requests():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    resp = s.send(prepped)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)

    # response api
    print(dir(resp))
    print(resp.reason)
    print(resp.history)
    print(resp.encoding)
    print(resp.content)
    print(resp.json())


if __name__ == '__main__':
    hard_requests()
