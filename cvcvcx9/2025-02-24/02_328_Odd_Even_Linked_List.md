```java

class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head; // 예외 처리
        
        ListNode odd = head;          // 홀수 노드 리스트의 시작점
        ListNode even = head.next;     // 짝수 노드 리스트의 시작점
        ListNode evenHead = even;      // 짝수 노드 리스트의 첫 번째 노드 저장
        
        while (even != null && even.next != null) {
            odd.next = even.next;      // 홀수 노드 연결
            odd = odd.next;            // 한 칸 이동
            even.next = odd.next;      // 짝수 노드 연결
            even = even.next;          // 한 칸 이동
        }
        
        odd.next = evenHead;           // 홀수 리스트 끝을 짝수 리스트 시작과 연결
        return head;
    }
}

```