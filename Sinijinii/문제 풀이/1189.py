R, C, K = map(int,input().split())
arr = list(list(input().strip()) for i in range(R))
vis = list([0 for _ in range(C)] for __ in range(R))

di = [0,0,1,-1]
dj = [1,-1,0,0]

# DFS는 재귀다
def dfs(sx,sy,dist):

    res = 0

    if sx == 0 and sy == C-1:
        if dist == K:
            return 1
        else:
            return 0

    vis[sx][sy] = 1

    for i in range(4):
        nx = sx+di[i]
        ny = sy+dj[i]

        if 0 <= nx < R and 0 <= ny < C:
            if vis[nx][ny] == 0 and arr[nx][ny] == ".":
                vis[nx][ny] = 1
                res += dfs(nx,ny,dist + 1)
                vis[nx][ny] = 0
                
    return res


print(dfs(R-1,0,1))
