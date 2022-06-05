## 다익스트라 알고리즘 사용 reference : https://www.youtube.com/watch?v=pORmQSzQCZk&t=365s

import pandas as pd
#from sklearn.metrics import plot_precision_recall_curve

filename = 'C:/Users/SAMSUNG/source/repos/Station_Edge/Station_Edge/edges.csv'
file = pd.read_csv(filename,encoding='UTF-8') 

class StationNode:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.prev = []
        self.next = []
        self.trsf = []
        self.time = 100000
    def printnode(self):
        print("\"{}({})\"".format(self.name,self.line),end='\t')
        print("prev=[",end='')
        if len(self.prev)!= 0:
            prev = self.prev[0]
            print("\"{}({}) : {}\"".format(prev.name,prev.line, self.prev[1]),end='')
        print("], next=[",end='')
        for j in range(len(self.next)):
            next = self.next[j]
            next2 = next[0]
            print("\"{}({}) : {}\"".format(next2.name,next2.line,next[1] ),end='')
        print("], trsf=[",end='')
        for j in range(len(self.trsf)):
            trsf = self.trsf[j]
            trsf1 = trsf[0]
            print("\"{}({}) : {}\"".format(trsf1.name,trsf1.line, trsf[1]),end='')
        print("]")

def append_next(self): 
    self.next.append([])
    return len(self.next)-1

def append_trsf(self):
    self.trsf.append([])
    return len(self.trsf)-1
        
def search_station(searchname, searchline=None):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    
    if searchline!=None and searchline>0 and searchline<=len(NodeList):
        for _, Stations in enumerate(NodeList):
            for j, station in enumerate(Stations):
                #station.printnode()
                #print("searchname{},{}/".format(type(searchname),searchname))
                #print("stationame{},{}/".format(type(station.name),station.name))
                #print("searchline{},{}/".format(type(searchline),searchline))
                #print("stationlin{},{}/".format(type(station.line),station.line))
                #print(station.name == searchname)
                #print(station.line == searchline)
                if (station.name == searchname) and (station.line == searchline):
                    # print("!!!!!!!!!!")
                    return station
    else:  #찾고자 하는 특정 호선이 존재 안 함.
        # print("NodeList={}".format(NodeList))
        for i, Stations in enumerate(NodeList):
            #print("i={}, Stations=  {}".format(i, Stations))
            #print("search from line#{}".format(i+1))
            for j, station in enumerate(Stations):
                if station.name == searchname:
                    return station
    return False


################ StationList Initialization ################

def getlinelist():
    #Data로 file 사용
    for (idx, row) in (file.iterrows()):
        idx = row[0]
        stationline = row[1]
        stationname = row[2]
        time = row[3]
        # print("rdline:\"{}\"".format(rdline))
        #print("{}".format(stationname))
        # print("stations={}".format(stations))
        while len(NodeList)<stationline:
            NodeList.append([])
        # print("stationline=",stationline)
            # print(NodeList)
        found = search_station(stationname,stationline)
                # print("i={}".format(i))
                # if(found!=False):
                #     print("found={}({})".format(found.name, found.line))
                # else:
                #     print("found={}".format(found))

                # 만약 새로운역이면 추가. 이미 존재하는역(현재 라인 내에서 한정)일경우 패스
        if found == False:  # new station in current line
            if(stationline != file.iloc[idx-1,1]):       #시작점 (호선이 달라지는 경우)
                newnode = StationNode(stationname, stationline)
                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에 추가##
                trsffound = search_station(stationname)
                if trsffound != False:
                    edge = 3
                    i = append_trsf(newnode)
                    j = append_trsf(trsffound)
                    newnode.trsf[i].append(trsffound)
                    trsffound.trsf[j].append(newnode)
                    newnode.trsf[i].append(edge)
                    trsffound.trsf[j].append(edge)
                    #print(newnode.trsf)
                    #print(trsffound.trsf)
            ##################################################
                #NodeList[stationline-1].append(newnode)

            else:      # 그냥 중간역
                newnode = StationNode(stationname, stationline)
                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에 추가##
                for checkline in range(1,stationline):
                    trsffound = search_station(stationname,checkline)
                    if trsffound != False:
                        #print("{}/{} in {}".format(trsffound.name, trsffound.line, checkline))
                        edge = 3
                        i = append_trsf(newnode)
                        j = append_trsf(trsffound)
                        newnode.trsf[i].append(trsffound)
                        trsffound.trsf[j].append(newnode)
                        newnode.trsf[i].append(edge)
                        trsffound.trsf[j].append(edge)
                        #print(newnode.trsf)
                        #print(trsffound.trsf)
                        ###################################################
                prevstation = search_station(file.iloc[idx-1,2],file.iloc[idx-1,1])
                #print(prevstation)
                i = append_next(prevstation)
                prevstation.next[i].append(newnode)
                newnode.prev.append(prevstation)
                prevstation.next[i].append(time)
                newnode.prev.append(time)
                prev = newnode.prev[0]

        NodeList[stationline-1].append(newnode)
       
        # print("-------------------------------------------")
        # for i,NodeLine in enumerate(NodeList):
        #     for j, Node in enumerate(NodeLine):
        #         Node.printnode()
        # print("-------------------------------------------")
        # input()
############################################################


NodeList = []
getlinelist()


##2호선 순환

ttukseom = search_station("뚝섬",2)
seongsu = search_station("성수",2)
ttukseom.prev.append(seongsu)
ttukseom.prev.append(1)
seongsu.next.append([])
seongsu.next[0].append(ttukseom)
seongsu.next[0].append(1)

############ search_station ############
## let's try testing search function! change "을지로" to another station name.
## Because "을지로" doesn't exist, {search_result} shows name "NotFound".
## If you change it to existing name, then you can get right result.

# search_result = search_station("방화")
#for i,NodeLine in enumerate(NodeList):
#    for j, Node in enumerate(NodeLine):
#        Node.printnode()

## dir : 경로 배열, nodename:탐색 경로 출발지, end : 도착지, time : 현재 경로(dir)가 가진 소요시간

def search(dir, nodename, end ,nodeline = 0, time = 0):

    ## 현재 노드에 저장되어 있는 최단 경로의 시간(StationNode class의 time 변수)과 비교했을 때,
    ## 현재 경로의 시간이 더 적으면 node.time 갱신, 아닐시 return 0
    if nodeline == 0: 
        node = search_station(nodename)
    else :
        node = search_station(nodename, nodeline)

    if node.time > time:
        node.time = time
        dir.append(node)
    else:
        return 

    if (node.name == end): #도착시 코드 종료
        for node in dir:
            print("{}({})".format(node.name, node.line), end = '->')
        print(time, "도착")
        return '도착'

    ## 다음 탐색 지점 설정, prev, next, trsf를 포함하되 바로 직전 노드는 제외함.
    ## ex : 개봉(1) -> 구일(1)일 경우, 구일(1)의 탐색 지점에서 개봉(1) 제외 
    next_direction = node.next
    prev = []
    prev.append(node.prev)
    if len(node.prev) != 0 and len(node.next) != 0:
        next_direction = next_direction + node.trsf + prev
    #print("{}({})->".format(node.name, node.line))
    
    if len(dir) >= 2:
        prev_path = dir[len(dir)-2]
        #print("이전 {}({})".format(prev_path.name, prev_path.line))
        #print(next_direction)
        for direction in next_direction:
            direction_name = direction[0]
            if direction_name.name == prev_path.name:
                #print("삭제 {}({})".format(direction_name.name, direction_name.line))
                next_direction.remove(direction)
            if next_direction == False:
                break
        #print(next_direction)
    
    #print("#######################")

    ## 아까 설정한 탐색 지정에 대해 탐색함. 환승(현재 name과 다음 탐색지의 name이 같음)을 제외하고
    ## 탐색지의 name이 경로 안에 있을 시, cycle을 이룬다고 판단. 경로 종료
    if len(next_direction) != 0:
        for next in next_direction:
            next_time = next[1]
            next = next[0]
            name = [ node.name for node in dir ]
            #print(" 목적지 : {}({}), 현재경로 : {}({})".format(next.name, next.line, name, node.line))
            if next.name in name:
                if name[len(name)-1] != next.name:
                    #print("cycle")
                    return 0
            search(list(dir), next.name, end, next.line ,time = time + next_time)

search([], '부평', '합정')
