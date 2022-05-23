# datastructure202201
   
   
> 각 역을 노드화(?)해서 NodeList에 넣었어요   
> 역명으로 노드 찾아내기 구현 성공했습니다.(뿌듯합니다..)   
> 현재 메인 파일은 prototype2.py 파일입니다.

---
## To Do List   
- [x] ~~각각의 역 데이터를 담아둘 NodeList 구현~~   
- [x] ~~텍스트파일에서 역 명들을 읽어오는 코드~~   
- [x] ~~역명으로 해당 노드 찾아내는 search function 구현~~   
- [ ] NodeList 방식을 바꾸기 -> 오직 Linked List 방식으로 구현해야함.   
        - text file에서 읽어오면서 append하는식으로..   
        - 어디분기점에 연결해야하는지는 새로운 search 함수를 사용해야함.   
          - 이때 search 함수는 StationNode 클래스에 포함시킨다.   
- [ ] 환승역 처리방식을 구상하기   
- [ ] "stations_Done_data_processing.txt" 토대로 NodeList에 집어넣기   
- [ ] spanning tree/BFS or DFS 사용하여 탐색알고리즘 구현   
   
   
---
**NodeList** 의 구조는 다음과 같습니다.   
   
NodeList = [ [ 1호선역1, 1호선역2, 1호선역3, ... ] , [ 2호선역1, 2호선역2,, ... ] , [ 3호선역1, 3호선역2,, ... ] , [...] , [...] ... ]   
즉,   
NodeList[0] = [ 1호선역1, 1호선역2, 1호선역3, ... ]   
NodeList[1] = [ 2호선역1, 2호선역2, 2호선역3, ... ]   
NodeList[2] = [ 3호선역1, 3호선역2, 3호선역3, ... ]   
...   
   
   
---
**n호선역m** 의 구조는 다음과 같습니다. 번호는 임의로 적었습니다. 실제데이터와 무관합니다.   
형태가 예쁘지않아서 수정해야할거같은데 일단은 계속 진행하겠습니다.   
   
cf) ...-월계-성북-석계-신이문-외대앞-...   
   
1호선역10 = [ {"name":"석계"}, next, prev }   
  - next = 1호선역9  (Node통째로)   
    - 1호선역9 = [ {{"name":"성북"}, next, prev }   
  - prev = 1호선역11 (Node통째로)   
    - 1호선역11 = [ {{"name":"신이문"}, next, prev }   

---
### 도움이되는 그림들?   
   
<img src="https://user-images.githubusercontent.com/60608787/169887176-507ef0b5-3251-4333-b775-108d97598fb7.png" width=75%>   
   
<img src="https://user-images.githubusercontent.com/60608787/169886693-7db83e11-105d-42d5-917f-245185379547.jpg" width=75%>   
