# -*- coding:utf-8 -*-
# A Python Object-Document-Mapper for working with MongoDB
# https://github.com/MongoEngine/mongoengine
__author__ = 'chen_ming'
__date__ = '2019-03-19 21:48'

from mongoengine import *
import datetime
connect('mydb')


class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    posted = DateTimeField(default=datetime.datetime.utcnow)
    tag = ListField(StringField(max_length=50))
    meta = {'allow_inheritance': True}


class TextPost(BlogPost):
    content = StringField(required=True)


class LinkPost(BlogPost):
    url = StringField(required=True)


post1 = TextPost(title='Using MongoEngine', content='See the tutorial')
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Docs', url='hmarr.com/mongoengine')
post2.tags = ['monogoengine', 'documentation']
post2.save()

for post in BlogPost.objects:
    print('===', post.title, '===')
    if isinstance(post, TextPost):
        print(post.content)
    elif isinstance(post, LinkPost):
        print('Link:', post.url)
    print()

print('Count all blog posts and its subtypes:')
print(BlogPost.objects.count())
print(TextPost.objects.count())
print(LinkPost.objects.count())

print('Count tagged posts:')
print(BlogPost.objects(tags='mongoengine').count())
print(BlogPost.objects(tags='mongodb').count())
