#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe36.py

problem = ('36. Find the sum of all numbers, less than one million, '
           'which are palindromic in base 10 and base 2.')

def is_palindrome(n):
    """Checks if number or string is a palindrome by comparing the first
    half to the reversed second half"""
    n = str(n)
    ln = len(n)
    return n[:ln//2 + ln%2] == n[ln//2:][::-1]

def solution(n=10**6):
    """
    Returns the sum of all numbers below n which are both palindromic in
    base 10 and base 2
    """
    return sum(x for x in xrange(n) if is_palindrome(x) and 
               is_palindrome(bin(x)[2:]))

if __name__ == '__main__':
    print problem
    print solution() # 872187
