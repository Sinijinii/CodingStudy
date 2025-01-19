## 접근방법
- 처음에는 큐로 하나씩 빼면서 접근해보려 했음
```py
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        queue = deque(nums)
        pointer = 1
        while queue and pointer < len(queue):
            tmp_num = queue.popleft()
            if tmp_num + queue[pointer] == k:
                queue.pop(pointer)
            else:
                pointer += 1

```

- 그러나 더 복잡해짐 그냥 투포인터로 푸는게 더 낫다고 생각되어 다시 풀어봄
- 왼쪽과 오른쪽을 설정하고, 서로 더해서 k가 되면 카운터를 하나 올리고
- 왼쪽포인터와 오른쪽 포인터를 하나씩 이동시킴
- 만약 k와 일치하지 않는다면 크기를 비교하여 왼쪽포인터 또는 오른쪽 포인터를 이동시킴

```py
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0 
        right = len(nums) - 1
        operation = 0 

        while left < right:
            if ((nums[left] + nums[right]) == k):
                operation += 1
                left +=1 
                right -=1
            elif((nums[left] + nums[right]) < k):
                left += 1
            else:
                right -= 1
        return operation
```