#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc7.py

import urllib, cStringIO, re
from PIL import Image

title = 'smarty'
url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
img_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
description = ('Image on page has a strip of altered pixels running '
               'horizontally through the middle.')

def solution():
    img_file = urllib.urlopen(img_url)
    # buffer file with cStringIO to keep in memory rather than saving it
    img_buff = cStringIO.StringIO(img_file.read())
    im = Image.open( img_buff )
    w, h = im.size
    x, chars = 0, []
    r, g, b = im.getpixel((x, h//2))[:3]
    while r == g == b and x < w:
        chars.append(r)
        x += 7 # increments by 7 pixels
        r, g, b = im.getpixel((x, h//2))[:3]
    message = ''.join([chr(x) for x in chars])
    print message # '[105, 110, 116, 101, 103, 114, 105, 116, 121]'
    word = ''.join([chr(int(x)) for x in re.findall(r'(\d+)', message)])
    split_url = url.split('/')
    document = split_url.pop(-1) # 'oxygen.html'
    doctype = document.split('.')[-1] # 'html'
    split_url.append( '.'.join([word, doctype]) )
    return '/'.join(split_url)

if __name__ == '__main__':
    print '7.', title, url, description
    print solution()
