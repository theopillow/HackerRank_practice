# Sample Input

# 6
# 3
# 5
# 4
# 7
# 2
# 1

# Sample Output

# 3 2 5 1 4 7 

import sys

class Node:
    def __init__(self, data):
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


    def levelOrder(self,root):
        leafs = [root]
        
        while len(leafs) > 0:
            leaf = leafs.pop(0)
            print(leaf.data, end=" ")
        
            if leaf.left:
                leafs.append(leaf.left)
            
            if leaf.right:
                leafs.append(leaf.right)
    
    
T = int(input())

myTree = Solution()

root = None

for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

myTree.levelOrder(root)