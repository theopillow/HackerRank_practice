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
        
#         if head == None:
#             head = self
#             head.data = data
#             head.next = None
#         else:
#             current = head
#             while current.next:
#                 current = current.next
#             current.next = Node(data)
#         return head


        n = Node(data)      
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = n
            return head
        else:
            return n

        
    #Complete this method
        
    
mylist= Solution()

T=int(input())
head=None

for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    

    mylist.display(head); 	  