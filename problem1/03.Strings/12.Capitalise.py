#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    w = s.split(" ")
    output = ""
    for i in w:
        output += i.capitalize() + " "
    return output  
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
