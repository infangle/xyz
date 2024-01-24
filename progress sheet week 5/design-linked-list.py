class Node:
    def __init__ (self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        while cur and index:
            cur = cur.next
            index -= 1
        return cur.val
        
    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else: 
            newNode.next = self.head
            self.head = newNode   
        
        self.size += 1 

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            prev = self.head
            while prev.next != None:
                prev = prev.next
            prev.next = newNode
            newNode.next = None
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        if index == 0:
            newNode.next = self.head
            self.head = newNode      
        else:
            prev = self.head
            while index - 1:
                prev = prev.next
                index -= 1
            newNode.next = prev.next
            prev.next = newNode 
        self.size += 1 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp = None
        else:
            prev = self.head
            i = 0
            while index - 1:
                prev = prev.next
                index -= 1
            next_node = prev.next
            prev.next = next_node.next
            del next_node
        
        self.size -= 1
                

            
            
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)