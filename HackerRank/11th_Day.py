#!/bin/python3

import math
import os
import random
import re
import sys

def sum_current_hourglass(array, row, col):
    sum_hourglass = 0
    sum_hourglass += array[row-1][col-1]
    sum_hourglass += array[row-1][col]
    sum_hourglass += array[row-1][col+1]
    sum_hourglass += array[row][col]
    sum_hourglass += array[row+1][col-1]
    sum_hourglass += array[row+1][col]
    sum_hourglass += array[row+1][col+1]
    return int(sum_hourglass)

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

# arr = [
#     [1,1,1,0,0,0],
#     [0,1,0,0,0,0],
#     [1,1,1,0,0,0],
#     [0,0,2,4,4,0],
#     [0,0,0,2,0,0],
#     [0,0,1,2,4,0]]

max_sum_hourglass = (-9*7)  # -63



for i in range(1,5):
    for j in range(1,5):
        sum_value = sum_current_hourglass(arr, i, j)
        if sum_value > max_sum_hourglass :
            max_sum_hourglass = sum_value

print(max_sum_hourglass)
