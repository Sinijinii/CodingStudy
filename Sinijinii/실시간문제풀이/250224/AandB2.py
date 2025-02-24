S = input()
T = input()
res = 0
def dfs(t):
    global res
    if t == S:
        res = 1
        return
    if len(t) == 0:
        return
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == "B":
        dfs(t[1:][::-1])

dfs(T)
print(res)