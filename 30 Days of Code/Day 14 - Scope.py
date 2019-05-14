## Sample Input

# 3
# 1 2 5

## Sample Output

# 4

class Difference:
    def __init__(self, a):
        self.__elements = a

# My Answer    
#     def computeDifference(self):
#         self.lst = []
#         self.__elements = a

#         for i in range(len(self.__elements) - 1):
#             for x in range(i + 1, len(self.__elements)):
#                 self.lst.append(abs(self.__elements[i] - self.__elements[x]))
        
#         self.maximumDifference = max(self.lst)

# Answer sheet
    def computeDifference(self):
        self.maximumDifference = abs(min(self.__elements) - max(self.__elements))
    
    def maximumDifference(self):
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)



