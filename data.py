from numpy import insert


class StationNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLinkedList():
    def __init__(self, station):
        self.head = StationNode(station)
        self.tail = self.head

    def push(self, station):
        if self.head == None:
            self.head = StationNode(station)
            self.tail = self.head
        else:
            current = self.head
            while current.next != None:
                current = current.next
            insertnode = StationNode(station,prev=current)
            current.next = insertnode
            self.tail = insertnode
    
    def pop(self):
        current = self.head
        while current != None:
            current = current.next
    
    def printlist(self):
        current = self.head
        while current != None:
            print("{}".format(current.data))
            current = current.next


dllist = DLinkedList(1111)
dllist.push(10)
dllist.push(20)
dllist.push(40)
dllist.push(30)
dllist.push(60)
dllist.push(50)

dllist.printlist()