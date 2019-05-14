# Sample Input

# 6

# Sample Output

# I implemented: AdvancedArithmetic
# 12 (1 + 2 + 3 + 6 = 12)



class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    
    def divisorSum(self, n):
        return sum([x for x in range(1, n+1) if n % x == 0])

n = int(input())

my_calculator = Calculator()

s = my_calculator.divisorSum(n)

print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)