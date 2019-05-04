#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0

for i in range(n):
    
    for j in range(n - 1):
        
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
    
print('Array is sorted in {} swaps.'.format(numberOfSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))


# Sample Input 0
# 3
# 1 2 3

# Sample Output 0
# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3
    
# Sample Input 1
# 3
# 3 2 1

# Sample Output 1
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3