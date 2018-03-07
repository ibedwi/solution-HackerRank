# TITLE : Diagonal Difference
#!/bin/python

import sys

def diagonalDifference(n,a):
    # Complete this function
    digKanan,digKiri = [0,0]
    for i in range(0,n):
        digKanan += a[i][i]
        digKiri += a[i][n-1-i]
    
    result =  abs(digKanan-digKiri)
    return result

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(n,a)
    print result
