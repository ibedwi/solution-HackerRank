# Title : Day 1: Interquartile Range

if __name__ == '__main__':
    N = int(raw_input())
    l = map(int,raw_input().split())
    j = map(int,raw_input().split())

    s = zip(l,j)
    s.sort()

    y = []
    for i in xrange(len(s)):
        for j in xrange(s[i][1]):
            y.insert(len(y),s[i][0] )
    
    jum = len(y)
    if jum%2 != 0 :
        Q2 = y[jum/2]
        L = y[0:(jum/2)]
        U = y[(jum/2)+1:]
        Q1 =(L[(len(L)-1)/2] + L[len(L)/2]) / 2.
        Q3 =(U[(len(U)-1)/2] + U[len(U)/2]) / 2.
    else :
        NQ2 = (jum+1) / 2
        Q2 = (y[jum/2] + y[jum/2 - 1]) / 2
        L = y[0:NQ2]
        U = y[NQ2:]
        Q1 =(L[(len(L)-1)/2] + L[len(L)/2]) / 2.
        Q3 =(U[(len(U)-1)/2] + U[len(U)/2]) / 2.

    print Q3 - Q1