#TITLE : Day 0: Mean, Median, and Mode

import numpy as np
from scipy import stats

if __name__ == '__main__':
    N = int(raw_input())
    int_list =  map(int, raw_input().split())
    
    # Mean Calculation
    mean = np.mean(int_list)

    # Median Calculation
    median = np.median(int_list)

    # Mode 
    mode_l = stats.mode(int_list)
    mode = int(mode_l[0])
    
    print mean
    print median
    print mode