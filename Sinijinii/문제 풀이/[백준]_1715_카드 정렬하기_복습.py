# n = int(input())

# card = []

# for c in range(n):
#     card.append(int(input()))

# card = sorted(card)
# res = 0
# while True:
#     if len(card) == 1:
#         break
#     res += card.pop(0)
#     res += card.pop(0)
#     card.append(res)
#     card = sorted(card)
# print(res)



from queue import PriorityQueue
n = int(input())

q = PriorityQueue() # 우선순위 큐

for i in range(n):
    q.put(int(input()))

res = 0
while True:
    if q.qsize() == 1:
        break
    res_min = q.get() + q.get()
    res += res_min
    q.put(res_min)

print(res)