#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe1.py

problem = ('1. Add all the natural numbers below one thousand that are '
           'multiples of 3 or 5.')

def solution():
    return sum(x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
    print problem
    print solution() # 233168
