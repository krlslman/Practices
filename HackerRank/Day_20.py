#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input().strip())
a = list(map(int, input().rstrip().split()))

totalNumberOfSwaps = 0
for i in range(n):  
    numberOfSwaps = 0   
    for j in range(n-1):
        if a[j] > a[j+1] :  # means there is something to change
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numberOfSwaps += 1
    totalNumberOfSwaps += numberOfSwaps
    if numberOfSwaps == 0:  # means there is nothing to change anymore
        break 
    
print("Array is sorted in", str(totalNumberOfSwaps), "swaps.")
print("First Element:", str(a[0]))
print("Last Element:", str(a[n-1]))
