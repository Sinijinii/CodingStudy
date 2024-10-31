li = input()
stack = []
res = 0

for idx in range(len(li)):
    if li[idx] == '(': # 열린 괄호는 추가
        stack.append('(')
    else: # 닫는 괄호")"
        stack.pop()
        if li[idx-1] == '(': # 레이저인 경우
            res += len(stack)
        # 막대 끝인 경우
        else: res += 1 

print(res)