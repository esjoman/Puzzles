#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe3.py

problem = ('3. What is the largest prime factor of the number '
           '600851475143 ?')

def is_prime(n):
    """Checks if n is a prime number"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    """
    Generates prime numbers in ascending order, rather than use a lookup
    table.
    """
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2

def prime_factors(n):
    """Returns list of prime factors as tuples (prime, power)."""
    result = []
    if n >= 2:
        for p in primes():
            count = 0
            while n % p == 0:
                n /= p
                count += 1
            if count:
                result.append((p, count))
            if n == 1:
                break
    return result

def solution(n=600851475143):
    """Returns the largest prime factor of n"""
    return max(prime_factors(n))[0]

if __name__ == '__main__':
    print problem
    print solution() # 6857
