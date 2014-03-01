#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Puzzles.py
#
#  This file serves as a demonstration which provides a command line 
#  user interface to select various puzzle solutions. The user can run 
#  individual problems, or run complete problem sets at once and time 
#  them.
#

import os
import time

ROOT_DIR = '.'

def run(filename, path, timed=False):
    print '\n[Running %s/%s]' % (path, filename)
    var = dict(locals(), **globals())
    if timed: 
        start = time.time()
        execfile(os.path.join(path, filename), var, var)
        print '(Solved in: %fs)\n' % (time.time() - start)
    else:
        execfile(os.path.join(path, filename), var, var)

def main():
    dirs = [d for d in os.walk(ROOT_DIR).next()[1] if not d[0] == '.']
    # Select category loop
    while True:
        print '\nCategories:'
        print ', '.join(['%d: %s' % (x, y) for x, y in enumerate(dirs)])
        cat = raw_input('Select a category by entering its preceding '
                        'number (or Q to quit):\n')
        if cat == 'Q': return
        try:
            if int(cat) < 0: raise ValueError
            d = dirs[int(cat)]
        except (IndexError, TypeError, ValueError):
            print '%r is invalid. Try again!' % cat
            continue
        
        # Select problem(s) loop
        while True:
            print '\n%s has the following problems available:' % d
            path = os.path.join(ROOT_DIR, d)
            files = [f for f in os.walk(path).next()[2] if f[-3:] == '.py']
            files.sort(key=lambda f: int(filter(lambda c: c.isdigit(), f)))
            probnums = [filter(lambda c: c.isdigit(), f) for f in files]
            print ', '.join(probnums)
            prob = raw_input('Select a problem by entering its number, '
                             'ALL to run all, TIMEALL to run all with '
                             'a timer, B to go back (or Q to quit):\n')
            if prob == 'ALL' or prob == 'TIMEALL':
                for f in files:
                    run(f, path, timed=(prob=='TIMEALL'))
            elif prob == 'B': break
            elif prob == 'Q': return
            elif prob in probnums:
                filename = files[probnums.index(prob)]
                run(filename, path)
            else:
                print '%r is invalid. Try again!' % prob

if __name__ == '__main__':
    main()
    print 'Goodbye!'
