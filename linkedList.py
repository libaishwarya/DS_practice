class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def linkedListIsempty(self,data): 
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            if temp.next is None:
                temp.data = data
                temp.next = Node(data)
        
    def print_elements(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            print("LL exists")
    

LL = LinkedList()
LL.linkedListIsempty(1)

LL.print_elements()