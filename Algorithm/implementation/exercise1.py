# TITLE : Grading Students

#!/bin/python

import sys
import math

def solve(grades):
    # Complete this function
    n = len(grades)
    solved_grades=[]
    base = 5
    for i in xrange(n):
        curRound5 = int(base * math.ceil(float(grades[i])/base))
        if (curRound5-grades[i]) > 2 or grades[i] < 38 :
            solved_grades.append(grades[i])
        else:
            solved_grades.append(curRound5)
    
    return solved_grades

if __name__ == "__main__":
    n = int(raw_input().strip())
    grades = []
    grades_i = 0
    for grades_i in xrange(n):
        grades_t = int(raw_input().strip())
        grades.append(grades_t)
    result = solve(grades)
    print "\n".join(map(str, result))


