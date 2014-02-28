#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc6.py

import urllib, cStringIO
from zipfile import ZipFile
from sys import stdout

title = 'now there are pairs'
url = 'http://www.pythonchallenge.com/pc/def/channel.html'
zip_url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
description = ('The image on the page is of a zipper, implying a '
               'zipped file, which can be accessed by changing .html '
               'to .zip')
hint = 'hint1: start from 90052. hint2: answer is inside the zip.'

def nothing_zip(next='90052'):
    """
    Iterates through linked list in zip file, gathering comment metadata
    on each file as it goes along. Returns aggregate comments.
    """
    remotezip = urllib.urlopen(zip_url)
    # buffer file with cStringIO to keep in memory rather than saving it
    zipinmemory = cStringIO.StringIO(remotezip.read())
    comments = ''
    with ZipFile(zipinmemory, 'r') as zip_file:
        while next and next.isdigit():
            filename = next + '.txt'
            comments += zip_file.getinfo(filename).comment
            with zip_file.open(filename, 'r') as f:
                data = f.read()
                next = data.split()[-1]
                print data, '          \r',
                stdout.flush()
    print '' # clears carriage return
    return comments

def solution(start='90052'):
    print nothing_zip(start) # spells 'hockey' using letters in 'oxygen'
    split_url = url.split('/')
    document = split_url.pop(-1) # 'channel.html'
    doctype = document.split('.')[-1] # 'html'
    split_url.append( '.'.join(['oxygen', doctype]) )
    return '/'.join(split_url)

if __name__ == '__main__':
    print '6.', title, url, description, hint
    print solution()
