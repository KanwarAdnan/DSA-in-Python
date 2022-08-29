class Node:
    def __init__(self,data,link = None):
        self.data = data
        self.link = link
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtHead(self,value):
        temp = Node(value)
        temp.link = self.head
        self.head = temp
        
        
    def isEmpty(self):
        return (self.head == None)
        
    def insertAtLast(self,value):
        temp = Node(value)
        if (self.isEmpty()):
            self.head = temp
        else:
            temp2 = self.head;
            while (temp2.link != None):
                temp2 = temp2.link
            temp2.link = temp
    
    def print(self):
        temp = self.head
        while (temp != None):
            print(f"{temp.data}->" , end='')
            temp = temp.link
        print("NULL\n")
        
    def removeAtHead(self):
        if (self.isEmpty()):
            return
        elif (self.head.link == None):
            self.head = None
        else:
            self.head = self.head.link
    
    def removeAtLast(self):
        if (self.isEmpty()):
            return
        elif (self.head.link == None):
            self.head = None
        else:
            temp = self.head
            while (temp.link.link != None):
                temp = temp.link
            temp.link = None
l1 = LinkedList()
l1.insertAtHead(1)
l1.insertAtHead(2)
l1.insertAtLast(0)
l1.print()
l1.removeAtLast()
l1.removeAtHead()
l1.print()
