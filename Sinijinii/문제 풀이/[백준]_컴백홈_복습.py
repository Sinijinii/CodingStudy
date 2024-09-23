R, C, K = map(int,input().split())
arr = list(list(input().strip()) for i in range(R))
vis = list([0 for _ in range(C)] for __ in range(R))

di = [0,0,1,-1]
dj = [1,-1,0,0]

# dfs 재귀
def dfs(sx,sy,dist):

    result = 0

    # 만약 집에 도착했을때
    if sx == 0 and sy == C-1:
        # 길이가 K라면?
        if dist == K:
            # 가능 수+1
            return 1
        else: return 0


    vis[sx][sy] = 1

    for i in range(4):
        nx = sx + di[i]
        ny = sy + dj[i]

        # 범위 내에 있다면?
        if 0<= nx < R and 0<= ny <C:
            # 방문 여부 + 막혀있는지
            if vis[nx][ny] == 0 and arr[nx][ny] == '.':
                vis[nx][ny] = 1
                result += dfs(nx,ny, dist +1)
                # 다시 초기화
                vis[nx][ny] = 0

    # 최종값 return
    return result


print(dfs(R-1,0,1))