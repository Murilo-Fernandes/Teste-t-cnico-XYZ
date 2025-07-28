#!/bin/python3

import math
import os
import random
import re
import sys

def getMinEngines(sessionTimings):
    # Write your code here
    if not sessionTimings:
        return 0
    
    events = []
    
    for start, end in sessionTimings:
        events.append((start, 1))
        events.append((end, -1))
        
    events.sort(key=lambda x: (x[0], x[1]))
    
    engines = 0
    max_engines = 0
    
    for _, event in events:
        engines += event
        max_engines = max(max_engines, engines) 
        
    return max_engines

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sessionTimings_rows = int(input().strip())
    sessionTimings_columns = int(input().strip())

    sessionTimings = []

    for _ in range(sessionTimings_rows):
        sessionTimings.append(list(map(int, input().rstrip().split())))

    result = getMinEngines(sessionTimings)

    fptr.write(str(result) + '\n')

    fptr.close()
