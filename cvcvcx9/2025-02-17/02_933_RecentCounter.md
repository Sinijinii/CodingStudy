## 풀이코드
- 클래스구현문제로 링크드리스트를 이용하여 풀이이
```java
class RecentCounter {
    private LinkedList<Integer> queue = new LinkedList<>();
    public RecentCounter() {
        queue = new LinkedList<>();
    }
    
    public int ping(int t) {
        queue.offer(t);
        // queue의 가장 앞자리가 현재 들어오는 핑보다 3000 초과해서 작을경우
        // queue에서 제외외
        while(queue.peek() < t-3000){
            queue.pop();
        }
        return queue.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
```