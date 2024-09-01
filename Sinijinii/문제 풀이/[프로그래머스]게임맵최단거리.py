from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    vis = list(list(0 for _ in range(m)) for __ in range(n))
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    def bfs(sx,sy):
        Q = deque()
        Q.append((sx,sy))
        vis[sx][sy] = 1
        while Q:
            x,y = Q.popleft()

            for i in range(4):
                nx = x+di[i]
                ny = y+dj[i]

                if 0<=nx<n and 0<=ny<m:
                    if vis[nx][ny] == 0 and maps[nx][ny] == 1:
                        vis[nx][ny] = 1
                        Q.append((nx,ny))
                        maps[nx][ny] = maps[x][y] + 1

        if maps[n-1][m-1] == 1:
            return -1
        else:
            return maps[n-1][m-1]
    return bfs(0,0)