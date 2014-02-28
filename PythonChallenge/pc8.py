#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc8.py

import urllib, re, bz2
from HTMLParser import HTMLParser

title = 'working hard?'
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
auth_url = 'http://www.pythonchallenge.com/pc/return/good.html'
description = ('The HTML document of the problem contains one large '
               'comment containing an obfuscated username and '
               'password. The link on the bee image leads to another '
               'page that requires a username and password.')
hint = ('Hint: inflate')

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
    text = parser.comments[0].decode('string_escape')
    un, pw = re.findall(r"\'(.+)\'", text)
    un = bz2.decompress(un)
    pw = bz2.decompress(pw)
    return '%s un:%s pw:%s' % (auth_url, un, pw)

if __name__ == '__main__':
    print '3.', title, url, description, hint
    print solution()
