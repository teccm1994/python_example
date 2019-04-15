# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-26 19:15'

import itchat
import time

# 1.给文件助手发一条消息
# itchat.auto_login()
# itchat.send('Hello, filehelper', toUserName='filehelper')


# 2.回复发给自己的文本信息
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text
#
#
# itchat.auto_login()
# itchat.run()

# 3.群发助手
itchat.auto_login(True)

SINCERE_WISH = u'祝%s四月快乐！'

friend_list = itchat.get_friends(update=True)[:1]
for friend in friend_list:
    if friend['NickName'] == '刘新宇':
        itchat.send(SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
        time.sleep(.5)

