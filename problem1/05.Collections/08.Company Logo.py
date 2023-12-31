import math
import os
import random
import re
import sys
from collections import Counter
# using __name__ variable
if __name__ == '__main__':
    
    # taking input from user and sorting it
    s = input()
    s = sorted(s)
    
    # using counter method to find the frequency of each of the words
    f = Counter(list(s))
    
    # using for loop to print the three words with frequency
    for k, v in f.most_common(3):
        print(k, v)
