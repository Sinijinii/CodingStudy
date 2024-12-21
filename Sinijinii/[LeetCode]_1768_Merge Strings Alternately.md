# 문자합치기

## 문제풀이
- 번갈아가며 문자를 합친다.
- 이때 더 긴쪽의 문자를 뒤에 합친다.
- 두 문자의 가장 짧은 문자길이만큼 돌며 두 문자열을 번갈아가며 res에 합쳐준다.
- 그 후 더 긴 문자열의 뒷 부분을 합치는 방식

## 코드
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        res = ""
        for i in range(min(w1,w2)):
            res += word1[i]
            res += word2[i]
        
        if w1>w2:
            res += word1[w2:]
        elif w2>w1:
            res += word2[w1:]
        
        return res
```