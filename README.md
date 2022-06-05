# datastructure202201
   
   
> 현재 메인 파일은 **/data_~/MAP.py**와 **search_cha.py** 파일입니다.   

---
## To Do List   
- [x] ~~각각의 역 데이터를 담아둘 NodeList 구현~~   
- [x] ~~텍스트파일에서 역 명들을 읽어오는 코드~~   
- [x] ~~역명으로 해당 노드 찾아내는 search function 구현~~   
- [x] ~~NodeList 방식을 바꾸기 -> 오직 Linked List 방식으로 구현해야함.~~   
        - ~~text file에서 읽어오면서 append하는식으로..~~   
        - ~~어디분기점에 연결해야하는지는 새로운 search 함수를 사용해야함.~~   
- [x] ~~환승역 처리방식을 구상하기~~   
- [x] ~~"stations_Done_data_processing.txt" 토대로 NodeList에 집어넣기~~   
        - ~~아마 이 위쪽 두개는 NodeList방식을 바꾸면서 저절로 이루어질듯함.~~   
- [x] ~~getlinelist()의 조건문을 더 체계적으로 정리하여, 정보업데이트가 누락되는 현상을 해결해야함.~~   
         - ~~분기점or시작점인경우, 이미존재하는 역이름인경우<- 의심되는구간. 노드간의 연결이 이루어지지 않음.~~   
- [x] spanning tree / ~~DFS(변경됨->)~~ / 다익스트라 알고리즘을 사용하여 탐색알고리즘 구현.   
- [ ] 두가지 메인파일을 하나의 코드로 합쳐 정리.   
- [ ] 가능한경우, 자료구조를 더 깔끔하게 만들기. 현재 쓸데없는 연결이 보이는듯함.   
   
   
---
**NodeList** 의 구조는 다음과 같습니다.   
   
NodeList = [ [ 1호선역1, 1호선역2, 1호선역3, ... ] , [ 2호선역1, 2호선역2,, ... ] , [ 3호선역1, 3호선역2,, ... ] , [...] , [...] ... ]   
즉,   
NodeList[0] = [ 1호선역1, 1호선역2, 1호선역3, ... ]   
NodeList[1] = [ 2호선역1, 2호선역2, 2호선역3, ... ]   
NodeList[2] = [ 3호선역1, 3호선역2, 3호선역3, ... ]   
...   
   
   
---
**n호선역m** 의 구조가 변경되었습니다.(2022/06/06)   
차후 작성예정입니다.   
   
---
## 유용한 링크   
<a href src="https://m.map.naver.com/subway/subwayLine.naver?region=1000">네이버 지하철 노선도</a>
---
## 도움이되는 그림들?   
   
<img src="https://user-images.githubusercontent.com/60608787/169887176-507ef0b5-3251-4333-b775-108d97598fb7.png" width=75%>   
   
<img src="https://user-images.githubusercontent.com/60608787/169886693-7db83e11-105d-42d5-917f-245185379547.jpg" width=75%>   
