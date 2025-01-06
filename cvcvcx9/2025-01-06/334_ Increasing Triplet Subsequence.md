## 접근방법
- 가장 간단하게 처음엔 삼중포문으로 접근
- 그러나 시간초과가 나서, 이후 투포인터로 접근방법 변경


```py
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
```