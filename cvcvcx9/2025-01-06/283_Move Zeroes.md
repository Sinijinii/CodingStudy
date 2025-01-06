## 풀이방법
- 단순한 풀이를 생각해봐야한다.
- 0이 아니면 앞으로이동시키는 로직만 생각하면 된다.
- 다 옮기고 포인터 인덱스 이후의 값들을 전부 0으로 변환하면 끝이다.
```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for n in nums:
            if n != 0:
                nums[idx] = n
                idx += 1
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
```