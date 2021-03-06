# Sample Input

# 7
# 3
# 5
# 2
# 1
# 4
# 6
# 7

# Sample Output

# 3


class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data

class Solution:
   
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    
    def getHeight(self, root):
        # Write your code here        
        if root.left == None and root.right == None:
            return 0
        
        else:
            RHeight = 0
            LHeight = 0
            
            if root.left:
                LHeight = self.getHeight(root.left) + 1
            if root.right:
                RHeight = self.getHeight(root.right) + 1
            
            return max(RHeight, LHeight)

                
        
T = int(input())

myTree = Solution()

root = None

for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height = myTree.getHeight(root)
print(height)       