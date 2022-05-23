# datastructure202201
   
   
> 각 역을 노드화(?)해서 NodeList에 넣었어요   
> 역명으로 노드 찾아내기 구현 성공했습니다.   
   
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
