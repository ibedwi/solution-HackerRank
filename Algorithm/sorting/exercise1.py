# Intro to Tutorial Challenges

#!/bin/python

import sys

def introTutorial(V, arr):
    # Complete this function
    n = len(arr)
    for i in xrange(n):
        if V == arr[i]:
            return i
    return -1
    
if __name__ == "__main__":
    V = int(raw_input().strip())
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = introTutorial(V, arr)
    print result
