## 접근방법
- 최대힙을 이용해서 포인트가 큰 놈을 빼먹기 위해 음수로 저장
- 포지션 별, K 년이 지난 이후, 이런 조건들을 까다롭게 처리하는게 관건인 문제라고 생각함.
```py
# 코드를 작성해주세요
import heapq
N, K = map(int,input().split())
hq = [[] for _ in range(12)]
for _ in range(N):
    p, w = map(int,input().split())
    # heapq는 최소힙이므로, 최대힙으로 써먹기 위해 음수로 저장
    heapq.heappush(hq[p],-w)

# K년 뒤의 결과를 알기위해 반복을 K번시킴
for _ in range(K):
    for i in range(12):
        if hq[i]:
            tmp = heapq.heappop(hq[i])
            tmp_point = 0 if -tmp < 1 else -tmp
            heapq.heappush(hq[i],-(tmp_point-1))
result = 0
for i in range(1,12):
    if hq[i]:
        result += -hq[i][0]
print(result)

```
