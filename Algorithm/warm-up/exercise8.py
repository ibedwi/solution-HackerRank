# TITLE : Mini-Max Sum
#!/bin/python

import sys

def miniMaxSum(arr):
    # Complete this function
    n = len(arr)
    lSum = []
    for i in range(0,n):
        tempSum = 0
        for j in range(0,n):
            if i == j:
                pass
            else:
                tempSum += arr[j]

        lSum.append(tempSum)
    
    lSum.sort()
    minim = lSum[0]
    maxim = lSum[n-1]

    print minim,maxim
    pass 
        
if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    miniMaxSum(arr)

