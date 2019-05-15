# Sample Input

# 3
# 12
# 5
# 7

# Sample Output

# Not prime
# Prime
# Prime

import math

n = int(input())

for x in range(n):
    t = int(input())
    prime = True
    
    if t == 1 or (t > 2 and t % 2 == 0):
        prime = False
    
    else:
        for i in range(1, int(math.sqrt(t)/2) + 1):
            j = i * 2 + 1
            if t % j == 0:
                prime = False
                break;
    if prime:
        print('Prime')
    else:
        print('No prime')