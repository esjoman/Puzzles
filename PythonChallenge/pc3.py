#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc3.py

import urllib
import re
from HTMLParser import HTMLParser

title = 're'
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
description = ('The HTML document of the problem contains one large '
               'comment: <!--kAewtloYgcFQaJNhHVGxXDiQmzj ... -->')
hint = ('Hint: One small letter, surrounded by EXACTLY three big '
        'bodyguards on each of its sides.')

class CommentParser(HTMLParser):
    """
    Extends HTMLParser in order to store contents of all comments in 
    HTML document
    """
    comments = []
    def handle_comment(self, data):
        self.comments.append(data)


def solution():
    """Returns the url of the next problem"""
    parser = CommentParser()
    parser.feed(urllib.urlopen(url).read())
    text = parser.comments[0]
    # re matches a lowercase letter surrounded by no more and no less
    # than 3 uppercase letters
    pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
    split_url = url.split('/')
    document = split_url.pop(-1)  # 'equality.html'
    split_doc = document.split('.')
    split_doc[0] = ''.join(re.findall(pattern, text))  # 'linkedlist'
    split_url.append('.'.join(split_doc))
    return '/'.join(split_url)

if __name__ == '__main__':
    print '3.', title, url, description, hint
    print solution()
