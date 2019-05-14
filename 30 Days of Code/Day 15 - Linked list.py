# Sample Input

# The following input is handled for you by the locked code in the editor: 
# The first line contains T, the number of test cases. 
# The  subsequent lines of test cases each contain an integer to be inserted at the list's tail.

# 4
# 2
# 3
# 4
# 1

# Sample Output

# The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:

# 2 3 4 1

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None 

class Solution: 
    
    def display(self, head):
        current = head
    
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        n = Node(data)      
        
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = n
            return head
        
        else:
            return n

        
    
mylist= Solution()

T=int(input())
head=None

for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    

    mylist.display(head); 	  