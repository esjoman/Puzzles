#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc10.py

import urllib2
import base64
import re

title = 'what are you looking at?'
url = 'http://www.pythonchallenge.com/pc/return/bull.html'
data_url = 'http://www.pythonchallenge.com/pc/return/sequence.txt'
un, pw = ('huge', 'file')  # username and password from problem 8
description = ('Image on page displays a bull. Clicking on the bull '
               'links to "sequence.txt"')
hint = 'Hint: len(a[30]) = ?'

def get_request(url, un, pw):
    """Handles authorization, returns request"""
    request = urllib2.Request(url)
    b64str = base64.encodestring('%s:%s' % (un, pw)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % b64str)
    return request

def say(s):
    """
    Returns string of number of repetitions of character + that 
    character, repeated for however many different characters are used 
    in sequence. In other words, it "says" what it sees.
    """
    s = str(s)
    # separated grouping of numbers. e.g. '111221' -> ['111', '22', '1']
    separated = [m.group() for m in re.finditer(r'(\d)\1*', s)]
    return ''.join([str(len(x)) + x[0] for x in separated])

def sequence(n):
    """
    Sequence begins with 1. Each following member describes the 
    previous. E.g. at a[0] there is one 1, so a[1] is '1'+'1'='11'. at 
    a[1] there are two 1's, so a[2] is '2'+'1'='21'.
    """
    seq = [1] + [None]*(n - 1)  # init sequence of length n
    for i in xrange(1, n):
        seq[i] = say(seq[i - 1])
    return seq

def solution(n=30):
    """Returns the url of the next problem"""
    f = urllib2.urlopen(get_request(data_url, un, pw))
    print f.read()  # a = [1, 11, 21, 1211, 111221,
    seq = sequence(n + 1)
    split_url = url.split('/')
    document = split_url.pop(-1)  # 'bull.html'
    doctype = document.split('.')[-1]  # 'html'
    split_url.append('.'.join([str(len(seq[n])), doctype]))
    return '/'.join(split_url)

if __name__ == '__main__':
    print '10.', title, url, description, hint
    print solution()
