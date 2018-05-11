# TITLE : Time Conversion

#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    angka = s[0:8]
    waktu = s[8:10]
    
    ar = map(int, angka.split(':'))

    if waktu == "AM":
        if ar[0] == 12:
            konversi = '00' + angka[2:8]
        else:
            konversi = angka
    else:
        konversi = str(12+ar[0]) + angka[2:8]
        
            
        

    return konversi

if __name__ == "__main__":
    s = raw_input().strip()
    result = timeConversion(s)
    print(result)
