#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe4.py

problem = ('4. Find the largest palindrome made from the product of '
           'two 3-digit numbers.')

def is_palindrome(n):
    """Checks if number or string is a palindrome by comparing the first
    half to the reversed second half"""
    n = str(n)
    ln = len(n)
    return n[:ln//2 + ln%2] == n[ln//2:][::-1]

def solution():
    """Returns the largest product of two 3-digit numbers that is a 
    palindrome"""
    return max(x * y for x in xrange(100, 1000) for y in xrange(x, 1000)
               if is_palindrome(x * y))

if __name__ == '__main__':
    print problem
    print solution() # 906609 (913 * 993)
