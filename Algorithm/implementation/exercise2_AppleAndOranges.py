# TITLE: Apple and Orange

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print apples
    print oranges
    pass

if __name__ == '__main__':
    st = raw_input().split()
    # Starting point of Sam's house location
    s = int(st[0])
    # Ending location of Sam's houe location
    t = int(st[1])
    
    ab = raw_input().split()
    # Location of the Apple Tree
    a = int(ab[0])
    # Location of the Orange Tree
    b = int(ab[1])

    mn = raw_input().split()
    # Number of apple that fell from the tree
    m = int(mn[0])
    # Number of orange that fell from the tree
    n = int(mn[1])
    # Distance at which each apple falls from the tree
    apples = map(int, raw_input().rstrip().split())
    # Distance at which orange falls from the tree
    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)