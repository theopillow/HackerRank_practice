'''
Input format:
There are  lines of input, where each line contains  space-separated integers describing 2D Array ; 
every value in  will be in the inclusive range of  to .
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''

'''
We define an hourglass in  to be a subset of values 
with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
'''

import math
import os
import random
import re
import sys
import numpy as np


if __name__ == '__main__':
    arr = []
    

    for _ in range(6):
        arr.append(list(map(int, input("Input 6 space-separated integers: ").rstrip().split())))
    
    print(np.array(arr))
    
    lst = []
    
    for x in range(4):
        for y in range(4):
            
            print(arr[x][y], arr[x][y+1], arr[x][y+2])
            print(' ', arr[x+1][y+1])
            print(arr[x+2][y], arr[x+2][y+1], arr[x+2][y+2])
            
            lst.append(sum([arr[x][y], arr[x][y+1], arr[x][y+2], 
                            arr[x+1][y+1],
                            arr[x+2][y], arr[x+2][y+1], arr[x+2][y+2]]))
            
    print('Maximum hourglass: %i' %max(lst))