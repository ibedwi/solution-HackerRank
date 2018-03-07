# TITLE : Simple Array Sum

#!/bin/python

import sys

def simpleArraySum(n, ar):
    # Complete this function
    result = 0
    for i in xrange(n):
        result = result + ar[i]
    
    return result

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
