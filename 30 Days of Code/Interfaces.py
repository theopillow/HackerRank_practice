class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

import math       
class Calculator(AdvancedArithmetic):
    
    def divisorSum(self, n):
        divs = [1]
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if n%i == 0:
                divs.extend([i, n/i])
        
        divs.append(n)
        
        return int(sum(list(set(divs))))


n = int(input())

my_calculator = Calculator()

s = my_calculator.divisorSum(n)

print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)