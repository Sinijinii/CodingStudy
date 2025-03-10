## 풀이방법
- 싱글링크드리스트를 순회하여 리스트에 저장
- 이후 리스트를 순회하면서 맥스값을 찾아냄


## 풀이코드
```java
class Solution {
    int maxStep = 0;
    public int longestZigZag(TreeNode root) {
        dfs(root, true, 0);
        dfs(root, false, 0);
        return maxStep;
    }
    private void dfs(TreeNode root, boolean isLeft, int step) {
        if (root == null) return;
        maxStep = Math.max(maxStep, step); // 최대값을 갱신
        if (isLeft) {
            dfs(root.left, false, step + 1); // 시작이 왼쪽이었으면, 왼쪽을 탐색하기 시작
            dfs(root.right, true, 1); // 오른쪽부터 다시 시작 (isLeft는 이전의 값이 왼쪽인 경우 true)
        } else {
            dfs(root.right, true, step + 1); 
            dfs(root.left, false, 1); 
        }
    }
    
}
```