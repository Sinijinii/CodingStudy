## 풀이방법
- 싱글링크드리스트를 순회하여 리스트에 저장
- 이후 리스트를 순회하면서 맥스값을 찾아냄


## 풀이코드
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
    public int pairSum(ListNode head) {
        var list = new ArrayList<Integer>();
        ListNode cur = head;
        while (cur != null) {
            list.add(cur.val);
            cur = cur.next;
        }
        int s = 0, e = list.size() - 1, ans = 0;
        while (s < e) {
            ans = Math.max(ans, list.get(s++) + list.get(e--));
        }
        return ans;
        }
}
```