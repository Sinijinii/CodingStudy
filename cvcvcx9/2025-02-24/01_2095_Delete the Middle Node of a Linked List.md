```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        int cnt =0;
        ListNode cur = head;
        while (cur != null){
            cnt++;
            cur = cur.next;
        }
        cur = head;
        if(cnt == 1){
            return cur.next;
        }
        int n = (cnt/2)-1;
        for(int i =0; i<n; i++){
            cur = cur.next;
        }
        cur.next = cur.next.next;
        return head;
    }
}
```