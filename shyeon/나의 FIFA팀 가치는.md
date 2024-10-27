# 풀이
```python
from queue import PriorityQueue
import sys

input = sys.stdin.readline
arr = [0] + [PriorityQueue() for _ in range(11)]

N, K = map(int, input().split())
for _ in range(N):
    P, W = map(int, input().split())
    arr[P].put(-W)

for _ in range(K):
    for a in range(1, 12):
        if arr[a].qsize() == 0:
            continue
        s = -arr[a].get()
        if s >= 1:
            s -= 1
        arr[a].put(-s)

cnt = 0
for f in range(1, 12):
    if arr[f].qsize() == 0:
        continue
    cnt += -arr[f].get()
print(cnt)
```  
