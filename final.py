import pandas as pd

def StationDict(_station, _time):
    return {"station":_station, "time":_time}

class StationNode:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.time = 10000000
        self.prev = []
        self.next = []
        self.trsf = []
    def printnode(self):
        print("\"{}({})\"".format(self.name,self.line),end='\t')
        print("prev=[ ",end='')
        for _,prev in enumerate(self.prev):
            print("({}({})-{}) ".format(prev["station"].name, prev["station"].line, int(prev["time"])),end='')
        print("], next=[ ",end='')
        for _,next in enumerate(self.next):
            print("({}({})-{}) ".format(next["station"].name, next["station"].line, int(next["time"])),end='')
        print("], trsf=[ ",end='')
        for _,trsf in enumerate(self.trsf):
            print("({}({})-{}) ".format(trsf["station"].name, trsf["station"].line, int(trsf["time"])),end='')
        print("]")

    def append_prev(self,prevstation,time):
        self.prev.append(StationDict(prevstation,time))
    def append_next(self,nextstation,time):
        self.next.append(StationDict(nextstation,time))
    def append_trsf(self,trsfstation,time):
        self.trsf.append(StationDict(trsfstation,time))

def search_station(searchname, searchline=None):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    
    if searchline!=None and searchline>0 and searchline<=len(NodeList):
        for _, Stations in enumerate(NodeList):
            for j, station in enumerate(Stations):
                if (station.name == searchname) and (station.line == searchline):
                    return station
    else:  #찾고자 하는 특정 호선이 존재 안 함.
        for i, Stations in enumerate(NodeList):
            for j, station in enumerate(Stations):
                if station.name == searchname:
                    return station
    return False

def check_trsf(newnode, searchname):
    for checkline in range(1,newnode.line):
        trsffound = search_station(searchname, checkline)
        if trsffound:
            edge = 180
            newnode.append_trsf(trsffound, edge)
            trsffound.append_trsf(newnode, edge)

################ StationList Initialization ################

def getlinelist():
    #Data로 file 사용
    prev=StationNode("None","0")
    for (idx, row) in (file.iterrows()):
        stationline = row[0]
        stationname = row[1]
        time = row[2]

        while len(NodeList)<stationline:
            NodeList.append([])
        
        found = search_station(stationname,stationline)
        # 만약 새로운역이면 추가. 이미 존재하는역(현재 라인 내에서 한정)일경우 패스
        if found == False:  # new station in current line

            ##########################
            ##  본격적인 데이터 입력 코드 ##
            ##########################
            newnode = StationNode(stationname, stationline)
            if(stationline != prev.line):
                #시작점 (호선이 달라지는 경우)

                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에추가
                check_trsf(newnode, stationname)
                #NodeList에 새로운 노드 추가
                NodeList[stationline-1].append(newnode)
                prev = newnode
                
            else:
                #그냥 중간역

                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에추가
                check_trsf(newnode,stationname)
                ##이전역과 현재역을 연결
                prev.append_next(newnode, time)
                # "이전역에서오는시간=이전역으로가는시간"으로 가정하면
                newnode.append_prev(prev, time)
                #NodeList에 새로운 노드 추가
                NodeList[stationline-1].append(newnode)
                prev=newnode
        else:
            prev = found

                
############################################################
# 파일 전처리
filename = './edges_sec.csv'
file = pd.read_csv(filename,encoding='UTF-8')

# 맵 생성
NodeList = []
getlinelist()
## 2호선 예외항목 -> 뚝섬(2), 성수(2) 연결하기
DS = search_station("뚝섬",2)
SS = search_station("성수",2)
time=90
DS.append_prev(SS,time)
SS.append_next(DS,time)

# search_result = search_station("방화")
for i,NodeLine in enumerate(NodeList):
    for j, Node in enumerate(NodeLine):
        Node.printnode()

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
    if len(node.prev) != 0 and len(node.next) != 0:
        next_direction = next_direction + node.trsf + node.prev
    #print("{}({})->".format(node.name, node.line))
    
    if len(dir) >= 2:
        prev_path = dir[len(dir)-2]
        #print("이전 {}({})".format(prev_path.name, prev_path.line))
        #print(next_direction)
        for direction in next_direction:
            direction_name = direction['station']
            #print(direction_name)
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
            next_time = next['time']
            next = next['station']
            name = [ node.name for node in dir ]
            #print(" 목적지 : {}({}), 현재경로 : {}({})".format(next.name, next.line, name, node.line))
            if next.name in name:
                if name[len(name)-1] != next.name:
                    #print("cycle")
                    return 0
            search(list(dir), next.name, end, next.line ,time = time + next_time)

search([], '녹양', '미아')