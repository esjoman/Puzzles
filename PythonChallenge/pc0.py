#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc0.py

title = 'warming up'
url = 'http://www.pythonchallenge.com/pc/def/0.html'
description = 'Image on page displays "2^38" prominently.'
hint = 'Hint: try to change the URL address.'

def solution():
    """Returns the url of the next problem"""
    split_url = url.split('/')
    document = split_url.pop(-1)  # '0.html'
    doctype = document.split('.')[-1]  # 'html'
    split_url.append('.'.join([str(2**38), doctype]))
    return '/'.join(split_url)  # 274877906944.html to next problem

if __name__ == '__main__':
    print '0.', title, url, description, hint
    print solution()
