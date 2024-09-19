from queue import PriorityQueue
n = int(input())

q = PriorityQueue() # 우선순위 큐
count = 0 # 최소 비교 횟수를 담을 변수

for _ in range(n):
    q.put(int(input()))

# 우선순위 큐에 원소가 하나만 남을 때까지
while q.qsize() != 1:
    temp = q.get() + q.get() # 가장 작은 두 수를 더해서
    count += temp # count에 더해주고
    q.put(temp) # 더한 값을 다시 우선순위 큐에 넣어준다

print(count)