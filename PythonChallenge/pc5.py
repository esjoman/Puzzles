#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc5.py

import urllib, pickle
from HTMLParser import HTMLParser

title = 'peak hell'
url = 'http://www.pythonchallenge.com/pc/def/peak.html'
description = ('In the HTML document there is a "peakhell" tag with '
               'src="banner.p" which contains a pickled object.')
hint = 'Hint: pronounce it' # peak hell => pickle

class PeakhellParser(HTMLParser):
    """Extends HTMLParser, retrieves peakhell tag src"""
    peakhells = []
    def handle_startendtag(self, tag, attrs):
        if tag == 'peakhell':
            src = dict(attrs).get('src', '')
            self.peakhells.append(src)

def banner(lol):
    """
    Prints a banner by taking in a list of lines. Each line contains a 
    list of tuples describing how many times to repeat that character.
    """
    result = ''
    for line in lol:
        for c in line:
            result += c[0] * c[1]
        result += '\n'
    print result

def solution():
    parser = PeakhellParser()
    parser.feed( urllib.urlopen(url).read() )
    split_url = url.split('/')
    document = split_url.pop(-1) # '0.html'
    pickle_url = '/'.join(split_url) + '/' + parser.peakhells[0]
    unpickle = pickle.load( urllib.urlopen(pickle_url) )
    banner(unpickle) # channel
    doctype = document.split('.')[-1] # 'html'
    split_url.append( '.'.join(['channel', doctype]) )
    return '/'.join(split_url)

if __name__ == '__main__':
    print '5.', title, url, description, hint
    print solution()
