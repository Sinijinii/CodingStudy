## 접근방법
- 큐를 사용하여 풀이
- for문을 한 번만 돌아서 해결해야 함

## 풀이코드
```py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = deque(list(s))
        for t_string in t:
            if len(s_list) == 0:
                return True
            if t_string == s_list[0]:
                s_list.popleft()

        print(s_list)
        if len(s_list) == 0:
            return True
        else:
            return False
```
