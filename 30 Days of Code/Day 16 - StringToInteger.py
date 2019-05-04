import sys

S = input().strip()

try:
    number = int(S)
    print(number)
    
except ValueError:
    print('Bad String')