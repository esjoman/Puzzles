#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc9.py

import urllib2
import base64
import re
import cStringIO
from HTMLParser import HTMLParser
from PIL import Image, ImageDraw

title = 'connect the dots'
url = 'http://www.pythonchallenge.com/pc/return/good.html'
img_url = 'http://www.pythonchallenge.com/pc/return/good.jpg'
un, pw = ('huge', 'file')  # username and password from problem 8
description = ('The image on the page has dots outlining some foliage. '
               'In the second comment of the HTML document are two '
               'lists of numbers labeled "first" and "second". '
               'By taking every two values as x and y coordinates, we '
               'are able to draw two continuous lines.')
hint = 'Hint: first+second=?'

class CommentParser(HTMLParser):
    """
    Extends HTMLParser in order to store contents of all comments in 
    HTML document
    """
    comments = []
    def handle_comment(self, data):
        self.comments.append(data)

def get_request(url, un, pw):
    """Handles authorization, returns request"""
    request = urllib2.Request(url)
    b64str = base64.encodestring('%s:%s' % (un, pw)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % b64str)
    return request

def solution():
    """Returns the url of the next problem"""
    parser = CommentParser()
    parser.feed(urllib2.urlopen(get_request(url, un, pw)).read())
    text = parser.comments[-1]
    first = re.findall(r'(\d+)', text.split('second:')[0])
    first = [int(x) for x in first]
    second = re.findall(r'(\d+)', text.split('second:')[1])
    second = [int(x) for x in second]
    size = max(first) + min(first)
    im = Image.new('RGBA', (size, size), 'white')
    draw = ImageDraw.Draw(im)
    # convert points to vectors. points a, b, c become a->b, b->c
    first_lines = [
        tuple(first[x:x+4]) for x in xrange(0, len(first)-2, 2)
    ]
    for line in first_lines:
        draw.line(line, fill=128)
    second_lines = [
        tuple(second[x:x+4]) for x in xrange(0, len(second)-2, 2)
    ]
    for line in second_lines:
        draw.line(line, fill=128)
    im.show()  # image resembles a bull ('cow.html' says it looks male)
    split_url = url.split('/')
    document = split_url.pop(-1)  # 'good.html'
    doctype = document.split('.')[-1]  # 'html'
    split_url.append('.'.join(['bull', doctype]))
    return '/'.join(split_url)  # 'bull.html'

if __name__ == '__main__':
    print '9.', title, url, description, hint
    print solution()
