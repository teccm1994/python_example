# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-17 14:41'

import requests


def download_image():
    """
    下载图片，文件
    :return: None
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'}
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552815093005&di=973f4d93d34b2f73e46052dc8bf16578&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201501%2F21%2F20150121112534_UMySU.jpeg"
    response = requests.get(url, headers=headers, stream=True)
    print(response.status_code)
    print(response.content)
    with open('demo.jpeg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    """
    下载图片，文件
    :return: None
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'}
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552815093005&di=973f4d93d34b2f73e46052dc8bf16578&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201501%2F21%2F20150121112534_UMySU.jpeg"

    # contextlib处理上下文
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        with open('demo1.jpeg', 'wb') as fd:
            for chunck in response.iter_content(128):
                fd.write(chunck)


if __name__ == '__main__':
    download_image_improved()
