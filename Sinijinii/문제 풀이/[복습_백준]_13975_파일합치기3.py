import heapq
import sys 


T = int(input())

for _ in range(T):
    k = int(input())
    li = list(map(int,input().split()))

    heapq.heapify(li)

    if k == 1:
        print(li[0])
        break
    res = 0 
    
    while len(li)>1:
        a = heapq.heappop(li)
        b = heapq.heappop(li)

        sum = a + b
        res += sum
        heapq.heappush(li,sum)

    print(res)