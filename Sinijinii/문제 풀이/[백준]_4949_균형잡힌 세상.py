import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()  # 입력 문자열을 받고 오른쪽 공백과 개행 문자를 제거
    if string == '.': break  # 문자열이 "."인 경우 반복문을 종료
    for s in string:
        if s not in '()[]':  # 괄호를 제외한 다른 문자들을 모두 제거
            string = string.replace(s, '')
    while '[]' in string or '()' in string:  # 문자열에 괄호 쌍이 있는 동안 반복
        string = string.replace('()', '')  # '()'를 제거
        string = string.replace('[]', '')  # '[]'를 제거
    print('no') if string else print('yes')
