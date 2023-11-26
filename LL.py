class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
    
class LL:
    def __init__(self):
        self.head = None
    
    def insertEnd(self,new_node):
        if self.head is None:
            self.head= new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node
            
    def insertFirst(self,new_node):
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        
     
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None  :
                break
            print(currentNode.data)
            currentNode = currentNode.next

node1 = Node("aishu")
linkedlist = LL()
linkedlist.insertEnd(node1)
node2 = Node("mohan")
linkedlist.insertEnd(node2)
node3 = Node("mom")
linkedlist.insertEnd(node3)
node4 = Node("dad")
linkedlist.insertEnd(node4)
node5 = Node("moh")
linkedlist.insertFirst(node5)
linkedlist.printList()
     