R,C,K = map(int,input().split())
li = [list(input().strip())for _ in range(R)]

di = [0,0,-1,1]
dj = [1,-1,0,0]

vis = [list([0]*C) for _ in range(R)]

def dfs(x,y,len_vis):

    res = 0

    if x == 0 and y == C-1:
        if len_vis == K:
            return 1
        return 0
    # 방문표시
    vis[x][y] = 1


    for i in range(4):
        nx = x + di[i]
        ny = y + dj[i]
        if 0 <= nx < R and 0 <= ny < C:
            if vis[nx][ny] == 0 and li[nx][ny] == '.':  # 장애물(T) 체크 추가
                res += dfs(nx, ny, len_vis + 1)
    # 방문 취소
    vis[x][y] = 0
    return res

print(dfs(R-1,0,1))