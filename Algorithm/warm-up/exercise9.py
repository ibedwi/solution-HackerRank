# TITLE : Birthday Cake Candles

#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    tertinggi = 0
    jumlah = 0
    for i in range(0,n):
        if ar[i]>tertinggi:
            tertinggi = ar[i]
            jumlah=1
        elif tertinggi == ar[i]:
            jumlah+=1
    
    return(jumlah)

if __name__ == "__main__":
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    result = birthdayCakeCandles(n, ar)
    print(result)
