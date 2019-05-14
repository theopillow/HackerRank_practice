# Sample Input

# 6
# 1
# 2
# 2
# 3
# 3
# 4

# Sample Output

# 1 2 3 4 

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None 

class Solution: 
    
    def insert(self, head, data):
            p = Node(data)           
            
            if head == None:
                head = p
            elif head.next == None:
                head.next = p
            else:
                start = head
                
                while(start.next != None):
                    start = start.next
                start.next = p
 
            return head
        
    def display(self, head):
        current = head
        
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        #Write your code here
        original = head
        
        while original:
            if original.next:
                if original.data == original.next.data:
                    original.next = original.next.next
                else:
                    original = original.next
                    
            else:
                original = original.next
        return head
        
        
mylist = Solution()
T = int(input())
head = None

for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)    

head = mylist.removeDuplicates(head)
mylist.display(head)