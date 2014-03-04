#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc11.py

import urllib2
import base64
import cStringIO
from PIL import Image

title = 'odd even'
url = 'http://www.pythonchallenge.com/pc/return/5808.html'
img_url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
un, pw = ('huge', 'file')  # username and password from problem 8
description = 'Image on page appears to be two images interlaced.'

def get_request(url, un, pw):
    """Handles authorization, returns request"""
    request = urllib2.Request(url)
    b64str = base64.encodestring('%s:%s' % (un, pw)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % b64str)
    return request

def solution():
    """Returns the url of the next problem"""
    img_file = urllib2.urlopen(get_request(img_url, un, pw))
    # buffer file with cStringIO to keep in memory rather than saving it
    img_buff = cStringIO.StringIO(img_file.read())
    im = Image.open(img_buff)
    w, h = im.size
    imdata = list(im.getdata())
    for i in xrange(1, w*h, 2):
        o = (i // w) % 2  # offset 0 or 1 every other line
        imdata[i - o] = (0, 0, 0)  # set to black
    im2 = Image.new(im.mode, im.size)
    im2.putdata(imdata)
    im2.show()  # can make out the word 'evil'
    split_url = url.split('/')
    document = split_url.pop(-1)  # '5808.html'
    doctype = document.split('.')[-1]  # 'html'
    split_url.append('.'.join(['evil', doctype]))
    return '/'.join(split_url)  # 'evil.html'


if __name__ == '__main__':
    print '11.', title, url, description
    print solution()
