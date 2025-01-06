## 접근방법
- 처음에 변수명에 그대로 대입하는 방법을 사용했는데, 틀렸음
- 검색해보니 변수명에 대입하는 방식은 실제로 주어진 배열의 값을 수정하는게 아니라 새로운 값을 대입
- 그래서 슬라이스를 통해 내부 값을 직접 변경시켜주어야 답이 나왔음


```py
class Solution:
    def compress(self, chars: List[str]) -> int:
        before = ""
        result = ""
        tmp_length = 1
        for char in chars:
            if before != char:
                if before != "":
                    result += before
                    if tmp_length > 1:
                        result += str(tmp_length)
                before = char
                tmp_length = 1
            else:
                tmp_length += 1
        result += before
        if tmp_length > 1:
            result += str(tmp_length)
        
        result = list(result)
        chars[:] = result
        return len(result)
```