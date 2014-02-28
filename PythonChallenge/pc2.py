#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc2.py

import urllib
from HTMLParser import HTMLParser

title = 'ocr'
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
description = ('The HTML document of the problem contains 2 comments: '
               '<!--find rare characters in the mess below:--> and '
               '<!--%%$@_$^__ ... %{(}$^$}*-->')
hint = ('Hint: recognize the characters. maybe they are in the book, '
        'but MAYBE they are in the page source.')

class CommentParser(HTMLParser):
    """
    Extends HTMLParser in order to store contents of all comments in 
    HTML document
    """
    comments = []
    def handle_comment(self, data):
        self.comments.append(data)


def solution():
    parser = CommentParser()
    parser.feed( urllib.urlopen(url).read() )
    mess = parser.comments[-1]
    split_url = url.split('/')
    document = split_url.pop(-1) # 'ocr.html'
    split_doc = document.split('.')
    split_doc[0] = filter(str.isalpha, mess) # 'equality'
    split_url.append( '.'.join(split_doc) )
    return '/'.join(split_url)

if __name__ == '__main__':
    print '2.', title, url, description, hint
    print solution()
