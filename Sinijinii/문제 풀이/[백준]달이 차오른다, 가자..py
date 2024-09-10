'''
빈 칸: 언제나 이동할 수 있다. ('.')
벽: 절대 이동할 수 없다. ('#')
열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f')
문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F')
민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0')
출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')
'''
'''
일단 가는건 그대로 설정
대신 갈 수 있는가에 대한 조건이 필요한것 같다.
1. 대문자인경우 소문자 열쇠를 가지고 있는가
2. # - 이동할 수 없음
3. 막힌길이면 되돌아가서 다시 시작해야함. vis를 어떻게 활용해야할까?
    - 열쇠의 유무
        1. 있는 경우: 가보자고~~
        2. 없는 경우: 어디서 다시 시작을 해야할까?
            - 처음 위치로?: 문이 있는 곳으로 가면 안되는데 이걸 어떻게 처리해야하나?
            
다른 사람 풀이 참조
- vis 반영할 때 그때 가지고 있는 key값을 반영(3차원)
    - 키의 유무에 따라 갈 수 있는지 없는지 갈리기 때문
- 열쇠의 유무를 비트마스크를 활용해서 관리한다.
'''

from collections import deque

N, M = map(int, input().split())
li = [list(input().strip()) for _ in range(N)]

# 64(2^6)개의 열쇠 상태에 대해 방문 여부를 체크할 3차원 배열로 변경
vis = [[[False] * M for _ in range(N)] for _ in range(1 << 6)]

sx, sy = False, False
for s in range(N):
    if '0' in li[s]:
        sx = s
        sy = li[s].index('0')

def bfs(sx, sy):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    Q = deque()
    Q.append((sx, sy, 0,0))  # 열쇠 리스트도 함께 저장
    vis[0][sx][sy] = True

    while Q:
        x, y, key, dist = Q.popleft()

        # print(key)

        if li[x][y] == '1':  # 출구에 도달하면 탈출
            return dist

        for i in range(4):
            nx, ny = x + di[i], y + dj[i]

            if 0 <= nx < N and 0 <= ny < M and not vis[key][nx][ny]:
                if li[nx][ny] == "#":
                    continue

                # 문인 경우 대응하는 열쇠가 있어야만 이동
                if 'A' <= li[nx][ny] <= 'F':
                    if key & (1 << (ord(li[nx][ny].lower()) - ord('a'))):
                        vis[key][nx][ny] = True
                        Q.append((nx, ny, key, dist + 1))

                # 열쇠를 얻은 경우
                elif 'a' <= li[nx][ny] <= 'f':
                    new_key = key | (1 << (ord(li[nx][ny]) - ord('a')))  # 새로운 열쇠 상태
                    if not vis[new_key][nx][ny]:  # 새로운 열쇠 상태로 방문한 적이 없으면
                        vis[new_key][nx][ny] = True
                        Q.append((nx, ny, new_key, dist + 1))

                # 빈 칸이거나 출구인 경우
                else:
                    vis[key][nx][ny] = True
                    Q.append((nx, ny, key,dist+1))

    return -1  # 탈출하지 못할 경우
print(bfs(sx, sy))
