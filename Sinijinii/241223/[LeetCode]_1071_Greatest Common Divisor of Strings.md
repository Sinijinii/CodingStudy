# 최대공약문자

## 문제 풀이
- t가 a번 반복되는 문자 배열은 str1 = t+t+t+t....+t => a*t
- t가 b번 반복되는 문자 배열은 str2 = t+t+t+...+t=> b*t

- 두 문자의 길이중 더 짧은 길이만큼 for문을 돌며 최대공약수를 체크한다.
- 최대 공약수를 구한 후 최대 공약문자를 판단한다(인덱스로)
- 그 최대공약문자가 반복되었을때 원 문자가 나오는지 판단한다.

## 코드
```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_s1, len_s2 = len(str1), len(str2)
        res = ''
        for i in range(1, min(len_s1, len_s2) + 1):
            if len_s1 % i == 0 and len_s2 % i == 0:
                temp = str2[:i]
                if temp*(len_s1//i) == str1 and temp*(len_s2//i) == str2:
                    res = temp
        return res
```