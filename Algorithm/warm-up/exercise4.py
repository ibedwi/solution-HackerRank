# TITLE : Mini-Max Sum

#!/bin/python

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    bigSum = 0L
    for i in xrange(n):
        bigSum += ar[i]
    
    return bigSum


n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
