## 풀이방법
- 문자열 앞 뒤를 바꾸는 방법

```py
class Solution:
    def reverseWords(self, s: str) -> str:
        tmp_list = list(s.split())
        tmp_list.reverse()
        print(tmp_list)
        return " ".join(tmp_list)
```