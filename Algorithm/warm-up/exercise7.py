# TITLE : Staircase

#!/bin/python

import sys


def staircase(n):
    # Complete this function
    for i in range(0,n):
        for j in range(n-1,i,-1):
            sys.stdout.write(' ')
        for k in range(-1,i):
            sys.stdout.write('#')
        print 
        
if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)
