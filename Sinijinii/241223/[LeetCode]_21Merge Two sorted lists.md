# 노드 리스트

## 문제 풀이
- 일반 리스트인줄 알았으나 전혀 다른 리스트였다.
- 노드 리스트가 무엇인지 개념이 잡혀있질 않아 어려움이 있었다.
- 해당 문제는 노드 리스트에 대한 사용법을 알아야 풀 수 있다고 생각하여 다른 코드를 찾아보았다.
- 코드 1
> 머지 소트의 병합처럼 두 리스트에 포인터를 두고 값을 비교해가며 결과 리스트에 넣게 됩니다. 
> 
> ans_head = ListNode(0) 부분을 넣어준 이유는 다음과 같습니다.
> 
> 결과 리스트를 만들 때 고정된 첫 헤드를 위해서 임의 값을 줍니다. 
> 
> 그리고 끝에 가서 return ans_head.next 로 답에 해당하는 부분만 리턴합니다.

- 코드 2
> l1.val 이 l2.val 보다 클 경우 두 개를 스왑 한다. 
> 
> 재귀 함수로 호출한 값을 l1.next에 할당하고 l1을 리턴한다.
> 
> l1이 None이 될 때까지 반복한다.


- 완벽한 이해가 되진 않았으나 이해 후 스스로 문제를 풀어봐야 할 것 같다.

---
## 코드 1
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        pointer_1 = list1
        pointer_2 = list2
        ans_head = ListNode(0)
        temp_head = ans_head

        while pointer_1 and pointer_2:
            if pointer_1.val <= pointer_2.val:
                temp_head.next = pointer_1
                temp_head = temp_head.next
                pointer_1 = pointer_1.next
            else:
                temp_head.next = pointer_2
                temp_head = temp_head.next
                pointer_2 = pointer_2.next

        if not pointer_1:
            temp_head.next = pointer_2
        else:
            temp_head.next = pointer_1

        return ans_head.next

```
## 코드 2
### 재귀 사용 풀이법
```python
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
```