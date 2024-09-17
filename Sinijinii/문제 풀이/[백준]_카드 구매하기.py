# 같은 카드를 한번만 살 수 있는 경우만 가능
# N = int(input())
# num = list(range(1,N+1))
# arr = list(map(int, input().split()))
# cnt = 0     # 합이 K가 되는 경우의 수
# res = 0
# for i in range(1<<N):   # 부분집합을 표시하는 i
#     s = 0       # 부분집합의 합
#     s_list = []
#     for j in range(N):  # j번 비트
#         if i&(1<<j):    # i의 j번 비트검사
#             s += num[j]   # 0이 아니면 j번 원소가 부분집합에 포함됨
#             s_list.append(arr[j])
#     if s==N:
#         if res <= sum(s_list):
#             res = sum(s_list)
#
# print(f'# {res}')
#





# i : 구하고 싶은 카드의 장수
# j : i보다 작은 카드의 장수
# dp : 카드비용의 최댓값을 저장하는 리스트
# j 와 어떤 x를 합쳤을 때 i가 나와야하기 때문에
# j + x = i 라는 식을 만족해야한다. 이 식을 정리하면 x의 값이 나온다.
# x = i - j (i > j)
# 따라서 조건을 만족하는 모든 j에 대해서 dp값을 비교해 주면 답이 나온다.

n = int(input())
# dp[i]는 카드가 i장 있을때의 최대비용
dp = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(max(dp))