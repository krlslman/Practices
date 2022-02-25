#!/bin/python3
# FIRST TRY : failed

import math
import os
import random
import re
import sys

n = int(input().strip())
def decimalToBinary(n):
    return bin(n).replace("0b", "")
text = str(decimalToBinary(n))

five = '11111'
four = '1111'
three = '111'
two = '11'
one ='1'
if five in text:
    print(len(five))
elif four in text:
    print(len(four))
elif three in text:
    print(len(three))
elif two in text:
    print(len(two))
elif one in text:
    print(len(one))

    
# SECOND TRY : succeed

import math
import os
import random
import re
import sys

n = int(input().strip())

def decimalToBinary(n):
    return bin(n).replace("0b", "")

text = str(decimalToBinary(n))

counter, result = 0, 0
for i in range(len(text)):
    if text[i] == '0':
        counter = 0
    else:
        counter += 1
        result = max(result,counter)
    
print(result)

 
