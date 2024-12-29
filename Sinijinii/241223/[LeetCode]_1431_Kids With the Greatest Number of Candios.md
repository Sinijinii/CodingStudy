# 최대 캔디

## 문제 풀이
- 주어진 최대 캔디를 우선 구한 후 캔디 리스트를 돌며 여분의 캔디를 더한 값과 최대 캔디의 값을 비교한다.

## 코드
```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res
        
```