# 나의 FIFA팀

## 풀이
- heap을 사용하여 각 포지션마다 가장 큰 가치를 뽑아냄
-포지션에 따른 선수 정보를 입력한다.
    빈 포지션이 있을 수 있음으로 0으로 초기화를 한다.
    heapq를 사용하여 선수의 가치를 음수로 저장한다.
- 8월에는 가치가 가장 높은 선수들의 가치를 1씩 감소시킨다.
    각 포지션마다 heappop을 사용해 가장 큰 가치를 뽑고 1을 감소시킨다.
    가치는 0보다 작지 않다. max(0, v)
- 11월에는 가치가 높은 선수를 재선출한다.
    8월에 선발되어 가치가 1씩 줄은 선수를 다시 선수풀에 넣음으로써(heappush) 해당 포지션의 가장 가치가 높은 선수를 0 인덱스 위치에 놓는다.
- k 년 동안 8월과 11월을 반복한다.
    각 포지션마다 0 인덱스에 위치한 선수들의 가치를 합산한다.

## heap
> 
    heapq.heappush(heap, item) : item을 heap에 추가
    heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
    heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )



## 코드
```
import sys
input = sys.stdin.readline  
import heapq

n, k = map(int, input().split())
members = [[0] for _ in range(12)] 

for i in range(n):
    p, w = map(int, input().split())  
    heapq.heappush(members[p], -w) 

# k년 동안 각 포지션에서 선수 가치 감소
for _ in range(k):
    for i in range(1, 12):  
        # 8월 가치 감소
        v = -heapq.heappop(members[i]) - 1
        v = max(0, v)
        # 11월 선수 재선출 (가치가 큰 숫자가 0 인덱스 위치로 이동)
        heapq.heappush(members[i], -v)

# k년 후에 각 포지션에서 가장 높은 가치를 가진 선수들의 가치 합산
res = sum(-members[i][0] for i in range(1, 12))

print(res)
```
