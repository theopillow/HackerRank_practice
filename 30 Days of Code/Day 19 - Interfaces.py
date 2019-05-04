class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    
    # Best solution
    def divisorSum(self, n):
        return sum([x for x in range(1, n+1) if n % x == 0])
    
#     def divisorSum(self, n):
#         total = n
#         for i in range(1, n):
#             if n % i == 0:
#                 total += i
#         return total


n = int(input())

my_calculator = Calculator()

s = my_calculator.divisorSum(n)

print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)