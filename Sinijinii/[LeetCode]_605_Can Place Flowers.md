# 꽃을 심을 수 있는가

## 문제 풀이
- 화단을 오른쪽에 하나 더 추가했다.
- 그 후 화단을 돌며 앞뒤 화단을 체크하며 꽃을 심을 수 있는지 판단한다.
- 예외를 처리해준다.
  - 첫번째 화단의 경우 뒷 화단만 0이면 심을 수 있다.
  - [0], n = 1인 경우
  

## 코드
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        r = 0
        res = False
        len_f = len(flowerbed)
        flowerbed.append(0)
        if sum(flowerbed) == 0 and len_f > 0 and n <2:
            return True
        for i in range(1,len_f):
            if r == n:
                res = True
                break
            if i == 1:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    flowerbed[0] = 1
                    r += 1
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    r += 1
        if r >= n:
            res = True
        
        return res

```