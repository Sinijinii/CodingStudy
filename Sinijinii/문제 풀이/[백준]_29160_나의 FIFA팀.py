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
