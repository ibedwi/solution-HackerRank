# TITLE : Plus Minus
#!/bin/python

import sys

def plusMinus(arr):
    n = len(arr)
    plus,minus,nol = [0,0,0]
    for i in range(0,n):
        if arr[i]<0:
            minus+=1
        elif arr[i]>0:
            plus+=1
        elif arr[i] == 0:
            nol+=1
    
    fMinus = minus/float(n)
    fPlus = plus/float(n)
    fNol = nol/float(n)

    print fPlus
    print fMinus
    print fNol
    return [fPlus,fMinus,fNol]

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)
