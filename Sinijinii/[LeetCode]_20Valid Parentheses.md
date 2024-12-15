# 괄호

## 문제 풀이
- 흔히 풀던 스택의 문제이다.
- 괄호 문자열을 순회한다.
- 여는 괄호가 나온다면 스택에 담아둔다.
- 닫는 괄호가 나온다면 스택 마지막값과 비교해서 짝이 맞다면 스택에서 꺼낸 후 계속 진행한다.
- 만약 1) 스택에도 없고 2) 닫는 괄호가 마지막값과 일치하지 않는다면 False를 반환한다.
- 순회가 끝난 후 스택이 비어있다면 성공이다.


```python
class Solution:
    from collections import deque
    def isValid(self, s: str) -> bool:
        par = {"(":")","[":"]","{":"}"}
        st = deque()
        for ss in s:
            if len(st) == 0 and ss in par.values():
                return False
            else:
                if ss in par:
                    st.append(par.get(ss))
                else:
                    if st[-1] == ss:
                        st.pop()
                    else:
                        return False        
        if len(st) == 0:
            return True
        else:
            return False
```