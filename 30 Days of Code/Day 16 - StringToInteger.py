# Sample Input 0
# 3

# Sample Output 0
# 3

# Sample Input 1
# za

# Sample Output 1
# Bad String

import sys

S = input().strip()

try:
    number = int(S)
    print(number)
    
except ValueError:
    print('Bad String')