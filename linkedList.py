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
    
    def addAtStart(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def addAtEnd(self,data):
        n=self.findLastNode()
        endNode = Node(data)
        n.next = endNode
        
    def findLastNode(self):
        current = self.head
        while(current.next):
            current = current.next
        return current
            
    def printLL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

LL = LinkedList()
LL.addAtStart(1)
LL.addAtStart(10)
LL.addAtStart(100)
LL.addAtEnd(50)
LL.printLL()