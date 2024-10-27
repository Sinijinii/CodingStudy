import heapq
import sys 

t = int(input())
for _ in range(t):
    k = int(input())
    li = list(map(int,sys.stdin.readline().split()))
    
    heapq.heapify(li)
    if k == 1:
        print(li[0])
        break
    res = 0
    while len(li)>1:
        a = heapq.heappop(li)
        b = heapq.heappop(li)
        sum = a+b
        res+=sum
        heapq.heappush(li,sum)
    print(res)