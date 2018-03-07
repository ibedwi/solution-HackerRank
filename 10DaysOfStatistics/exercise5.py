# TITLE : Day 1: Standard Deviation

import math as m

if __name__ == '__main__' : 
    N = int(raw_input())
    l = map(int,raw_input().split())

    # Create distance table
    mean = sum(l)/float(N)

    dt = []
    for i in xrange(N):
        dt.insert(len(dt), (l[i] - mean)**2 )

    std = m.sqrt(sum(dt) / N )

    print round(std,1)