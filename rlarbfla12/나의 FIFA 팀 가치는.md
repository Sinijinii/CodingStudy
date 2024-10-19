# 백준 29160번

```python
import heapq
import sys
input = sys.stdin.readline 

# N: 선수 수, K: 반복할 년 수
N, K = map(int, input().split())

# 각 포지션별 우선순위 큐(힙)를 초기화 
# 각 포지션에 (0, 0)을 초기값으로 넣어서 초기화
player = [[(0,0)] for _ in range(11)]

# 선수 정보 입력
for _ in range(N):
    P, W = map(int, input().split())  # P: 포지션 번호, W: 선수 가치
    # (음수로 된 선수 가치, 양수로 된 선수 가치)를 힙에 넣음 
    # heappop이 튜플의 첫번째 값을 기준으로 하기 때문
    heapq.heappush(player[P-1], (-W,W))

# K년 동안 반복
for _ in range(K):
    # 매년 각 포지션에 대해 가장 높은 가치를 가진 선수를 처리
    for i in range(11):
        # 각 포지션에서 가장 높은 가치를 가진 선수를 힙에서 꺼냄
        best = heapq.heappop(player[i])
        # 선수의 가치를 1 감소시키되, 0보다 작아지지 않도록 처리
        if best[1] - 1 < 0:  # 선수가 0 미만으로 떨어지면
            heapq.heappush(player[i], (0, 0))  # 가치가 0인 선수로 대체
        else:
            # 가치가 1 줄어든 선수를 다시 힙에 넣음
            heapq.heappush(player[i], (best[0] + 1, best[1] - 1))


# K년이 끝난 후, 각 포지션에서 가장 높은 가치를 가진 선수를 선택
total = 0
for i in range(11):
    # 각 포지션에서 가장 높은 가치를 가진 선수를 힙에서 다시 꺼냄
    best = heapq.heappop(player[i])
    total += best[1]  # 실제 가치(양수)만 합산


# 결과 출력 - K년 후 최종 팀의 총 가치
print(total)
```


```python
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
best = [[] for _ in range(12)]      # 각 포지션의 선수 가치 저장

for _ in range(n):
    p, w = map(int, input().split())
    heapq.heappush(best[p], -w)     # 선수 가치 음수로 저장(heapq 최솟값 뽑음)

for _ in range(k):      # k년 동안
    for i in range(1, 12):
        if best[i]:     # 포지션에 선수 있으면 가장 가치 큰 선수 뽑기
            player = heapq.heappop(best[i])
            if player < 0:      # 음수니까 가치 -1을 +로 함
                player += 1
            heapq.heappush(best[i], player)

worth = 0
for i in range(1, 12):
    if best[i]:
        worth += heapq.heappop(best[i])

print(abs(worth))

```
