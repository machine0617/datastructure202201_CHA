class StationNode:
    def __init__(self, data):
        self.data = data
        self.prev = []
        self.next = []

class DLinkedList():
    def __init__(self, station,transf_to=None):
        self.head = StationNode(station)
        self.tail = self.head
        if(transf_to!=None):
            self.next=transf_to     # transf_to = line number

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
        last = self.head.next
        while last.next != None:
            current = current.next
            last = last.next
        last=None
        current.next=None

    def printlist(self):
        current = self.head
        while current != None:
            print("{}".format(current.data))
            current = current.next

def search_station(line,name):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    # If station we want is found then now {target} is {StationList[i]}
    target=None
    return target

StationList=[]
def getlinelist():
    f=open("./stations.txt","r",encoding="UTF-8")
    line = f.readline().strip()
    while line != '':
        stations = line.split(",")
        StationList.append(stations)
        line = f.readline().strip()
    # print(StationList)
    f.close()

getlinelist()
for _, Stations in enumerate(StationList):
    print("{} : {}".format(_+1,Stations))
    NodeList=[]
    for i, station in enumerate(Stations):
        newnode = StationNode({"name":station})
        NodeList.append(newnode)
        if i>0:
            NodeList[i-1].next.append(newnode)
            newnode.prev.append(NodeList[i-1])
    # print(NodeList)
    for i, node in enumerate(NodeList):
        print("\"{}\"".format(node.data["name"]),end=' ')
        print("prev=[",end='')
        for j, prev in enumerate(node.prev):
            print("\"{}\"".format(prev.data["name"]),end='')
        print("], next=[",end='')
        for j, next in enumerate(node.next):
            print("\"{}\"".format(next.data["name"]),end='')
        print("]")