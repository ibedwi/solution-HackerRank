#TITLE : Day 1: Quartiles

if __name__ == '__main__':
    N = int(raw_input())
    l = map(int,raw_input().split())
    l.sort()
    print l
    if N%2 != 0 :
        Q2 = l[N/2]
        L = l[0:(N/2)]
        U = l[(N/2)+1:]
        Q1 =(L[(len(L)-1)/2] + L[len(L)/2]) / 2
        Q3 =(U[(len(U)-1)/2] + U[len(U)/2]) / 2
    else :
        NQ2 = (N+1) / 2
        Q2 = (l[N/2] + l[N/2 - 1]) / 2
        L = l[0:NQ2]
        U = l[NQ2:]
        Q1 =(L[(len(L)-1)/2] + L[len(L)/2]) / 2
        Q3 =(U[(len(U)-1)/2] + U[len(U)/2]) / 2
        
    print Q1
    print Q2
    print Q3