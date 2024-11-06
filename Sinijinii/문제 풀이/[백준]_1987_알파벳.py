def dfs(y, x, dist, check):
    cnt = dist

    for i in range(4):
        ny, nx = y + directy[i], x + directx[i]
        if 0 <= ny < r and 0 <= nx < c:
            tm = ord(arr[ny][nx]) - ord('A')
            if not check[tm]:
                check[tm] = 1
                cnt = max(cnt, dfs(ny, nx, dist + 1, check))
                check[tm] = 0

    return cnt

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

directy = [0, 0, -1, 1]  
directx = [-1, 1, 0, 0]

check = [0] * 26
check[ord(arr[0][0]) - ord('A')] = 1
print(dfs(0, 0, 1, check))