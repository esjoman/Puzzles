#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pc1.py

import string

title = 'What about making trans?'
#redirected from http://www.pythonchallenge.com/pc/def/274877906944.html
url = 'http://www.pythonchallenge.com/pc/def/map.html'
description = 'Image on page displays "K->M, O->Q, E->G" prominently.'
hint = 'Hint: everybody thinks twice before solving this.'
crypt = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq "
         "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw "
         "rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq "
         "pcamkkclbcb. lmu ynnjw ml rfc spj.")
"""Translates to:
i hope you didnt translate it by hand. thats what computers are for. 
doing it in by hand is inefficient and that's why this text is so long. 
using string.maketrans() is recommended. now apply on the url.
"""

def decrypt(s):
    """
    Replaces each letter with the letter 2 places down which wraps 
    around. E.g. K->M, O->Q, E->G
    """
    alphabet = string.ascii_lowercase   # 'abcdefghijklmnopqrstuvwxyz'
    trans = alphabet[2:] + alphabet[:2] # 'cdefghijklmnopqrstuvwxyzab'
    return s.translate(string.maketrans(alphabet, trans))

def solution():
    split_url = url.split('/')
    document = split_url.pop(-1) # 'map.html'
    split_doc = document.split('.')
    split_doc[0] = decrypt(split_doc[0])
    split_url.append( '.'.join(split_doc) )
    return '/'.join(split_url)

if __name__ == '__main__':
    print '1.', title, url, description, hint
    print crypt, '\nTranslates to:\n', decrypt(crypt)
    print solution()
