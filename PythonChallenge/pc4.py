#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc4.py

import urllib
from sys import stdout

title = 'follow the chain'
# http://www.pythonchallenge.com/pc/def/linkedlist.html simply displays
# linkedlist.php, so replaced it in the url
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
description = ('A link on the page queries ?nothing=12345, which '
               'produces a page stating "and the next nothing is '
               '44827"')

def nothing(next='12345'):
    """
    Traverses the linked list and returns the tail node. Through trial
    and error found special cases to check for. Prints out progress
    because it has to make so many requests, its speed is relient on
    latency and can potentially take a long time.
    """
    while next and next.isdigit():
        params = urllib.urlencode({'nothing': next})
        page = urllib.urlopen(url + '?' + params).read()
        if page == 'Yes. Divide by two and keep going.':
            next = str(int(next) / 2)
        else:
            next = page.split()[-1]
        print next, '     \r',
        stdout.flush()
    print ''  # clears carriage return
    return next

def solution(start='12345'):
    """Returns the url of the next problem"""
    split_url = url.split('/')
    split_url[-1] = nothing(start)  # peak.html
    return '/'.join(split_url)

if __name__ == '__main__':
    print '4.', title, url, description
    print solution()
