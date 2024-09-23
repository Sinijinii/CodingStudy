from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    
    vis = list([0 for _ in range(m)] for __ in range(n))
    
    Q = deque()
    res = 0
    
    def bfs(sx,sy,cnt):
        global res
        Q.append((sx,sy,cnt))
        vis[sx][sy] = 1
        
        while Q:
            x,y,c = Q.popleft()

            if x == n-1 and y == m-1:
                if res <= c:
                    res = c
            for i in range(4):
                nx = x + di[i]
                ny = y + dj[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if vis[nx][ny] == 0 and maps[nx][ny] == 1:
                        vis[nx][ny] = 1
                        Q.append((nx,ny,c+1))
                        
    bfs(0,0,1)
    print(res)
    return 

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])