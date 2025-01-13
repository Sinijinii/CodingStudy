## 접근방법
- 투포인터를 이용하여 풀이
- 왼쪽 기둥의 높이와 오른쪽 기둥의 높이를 비교하여 작은 높이를 구함
- 그 뒤, 오른쪽기둥 위치에서 왼쪽 기둥의 위치를 빼서 너비를 구함
- 곱하여 넓이를 구하고 최대 넓이를 저장함

## 풀이코드
```py

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
```