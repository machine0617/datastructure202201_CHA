class StationNode:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.prev = []
        self.next = []
        self.trsf = []
    def printnode(self):
        print("\"{}\"".format(self.name),end=' ')
        print("prev=[",end='')
        for j, prev in enumerate(self.prev):
            print("\"{}\"".format(prev.name),end='')
        print("], next=[",end='')
        for j, next in enumerate(self.next):
            print("\"{}\"".format(next.name),end='')
        print("]")
        
def search_station(searchname, searchline=None):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    
    if searchline!=None and searchline>0 and searchline<=len(NodeList):
        for _, Stations in enumerate(NodeList):
            for j, station in enumerate(Stations):
                if station.name is searchname and station.line is searchline:
                    return station
    else:
        # print("NodeList={}".format(NodeList))
        for i, Stations in enumerate(NodeList):
            print("i={}, Stations=  {}".format(i, Stations))
            print("search from line#{}".format(i+1))
            for j, station in enumerate(Stations):
                if station.name == searchname:
                    return station
    return False


################ StationList Initialization ################
def getlinelist():
    f=open("./stations_Done_data_processing.txt","r",encoding="UTF-8")
    rdline = f.readline().strip()
    stationline=0
    while rdline != '':
        print("rdline:\"{}\"".format(rdline))
        stations = rdline.split(",")
        print("stations={}".format(stations))
        if stations[0].isnumeric():
            print("stations[0].isnumeric()")
            stationline = int(stations[0])
            while len(NodeList)<stationline:
                NodeList.append([])
            print("stationline=",stationline)
            print(NodeList)
        else:
            for i, stationname in enumerate(stations):
                print("stationname=\"{}\"".format(stationname))
                found = search_station(stationname)
                if found is False:  # if new node
                    print("if found is False:")
                    if(i<=0): # if 분기점 or 시작점
                        newnode = StationNode(stationname, stationline)
                        NodeList[stationline-1].append(newnode)
                    else:
                        newnode = StationNode(stationname, stationline)
                        prevstation = search_station(stations[i-1])
                        newnode.prev.append(prevstation)
                        prevstation.next.append(newnode)
                        NodeList[stationline-1].append(newnode)
                else:   # if already exist station
                    print("else:")
                    if found.line is not stationline:   # another line station with same name
                        print("another line!")
                        newnode = StationNode(stationname, stationline)
                        NodeList[stationline-1].append(newnode)
                        found.trsf.append(newnode)
                        newnode.trsf.append(found)
        rdline = f.readline().strip()
    f.close()
############################################################


NodeList=[]
getlinelist()


############ search_station ############
## let's try testing search function! change "을지로" to another station name.
## Because "을지로" doesn't exist, {search_result} shows name "NotFound".
## If you change it to existing name, then you can get right result.
search_result = search_station("방화")
print("NodeList=")
print(NodeList)
print("result=name{},line{},prev{},next{},trsf{}".format(search_result.name, search_result.line, search_result.prev, search_result.next,search_result.trsf))