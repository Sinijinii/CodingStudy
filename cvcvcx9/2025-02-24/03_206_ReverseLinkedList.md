```
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;  // 이전 노드를 저장할 변수 (초기값은 null)
        ListNode cur = head;   // 현재 노드
        
        while (cur != null) {
            ListNode next = cur.next;  // 다음 노드를 임시 저장
            cur.next = prev;           // 현재 노드의 next를 이전 노드로 변경
            prev = cur;                // prev를 현재 노드로 이동
            cur = next;                 // cur을 다음 노드로 이동
        }
        return prev;  // prev가 새로운 head가 됨
    }
}

```