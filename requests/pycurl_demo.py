# -*- coding:utf-8 -*-
# http://pycurl.io/docs/latest/quickstart.html
# Python 3.6.1
__author__ = 'chen_ming'
__date__ = '2019-03-24 14:02'

import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.io/')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
print(body.decode('iso-8859-1'))
