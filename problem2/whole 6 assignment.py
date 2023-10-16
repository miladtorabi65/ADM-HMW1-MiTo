#This is homework1/problem2 of ADM subject-Sapienza University done by Milad Torabi.*****
#Problem 2 : the list of demanded tasks is below:
#1.birthday-cake-candles
#2.Number Line Jumps(kangaroo)
#3.strange-advertising
#4.recursive-digit-sum
#5.insertionsort1
#6.insertionsort2
#*********************************************************
#1.birthday-cake-candles • https://www.hackerrank.com/challenges/birthday-cake-candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candle_max=max(candles)
    num_candle_max=candles.count(candle_max)

    return num_candle_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
#*****************************************************************************************
#2.Number Line Jumps(kangaroo) • https://www.hackerrank.com/challenges/kangaroo

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return "YES"
    elif (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
        return "NO"
    elif (x2 - x1) % (v1 - v2) == 0: #the optimal instead of saying x1+(v1*i)==x2+(v2*i)
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
#******************************************************************************************
#3.strange-advertising • https://www.hackerrank.com/challenges/strange-advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    c=0 #as cumulative
    s=5 #as shared
    d=1 #as day
    
    while d<= n:
        liked=s//2
        c += liked
        s = liked*3
        d+=1
    
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
#**********************************************************************************************
#4.recursive-digit-sum https://www.hackerrank.com/challenges/recursive-digit-sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    r = str(sum(int(i) for i in n)* k)
    while True:
        r = str(sum(int(i) for i in r))
        if (len(r) == 1):
            break    
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
#**********************************************************************************************
#5.insertionsort1 • https://www.hackerrank.com/challenges/insertionsort1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    probe = arr[-1]
    for ind in range(len(arr)-2, -1, -1):
        if arr[ind] > probe:
            arr[ind+1] = arr[ind]
            print(" ".join(map(str, arr)))
        else:
            arr[ind+1] = probe
            print(" ".join(map(str, arr)))
            break
    if arr[0] > probe:
        arr[0] = probe
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
#*************************************************************
#6.insertionsort2 • https://www.hackerrank.com/challenges/insertionsort2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        print(*arr)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
#*********************************************************************************
