arr = input()
find_word = input()
T = True
res = 0
while T:
    if find_word in arr:
        arr = arr.replace(find_word,"*",1)
        res += 1
    else:
        T = False
print(res)