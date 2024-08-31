def dfs(current_y, current_x, current_distance, r, c, k):
    global cnt

    if current_y == 0 and current_x == c - 1:
        if current_distance == k:
            cnt += 1
        return

    for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
        ni, nj = current_y + di, current_x + dj
        if 0 <= ni < r and 0 <= nj < c and roads[ni][nj] != 'T' and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, current_distance + 1, r, c, k)
            visited[ni][nj] = 0


R, C, K = map(int, input().split())
roads = [list(input()) for _ in range(R)]

cnt = 0
visited = [[0] * C for _ in range(R)]
visited[R - 1][0] = 1
dfs(R - 1, 0, 1, R, C, K)
print(cnt)