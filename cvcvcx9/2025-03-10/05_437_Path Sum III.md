
```java
class Solution {
    int total = 0;
    public int pathSum(TreeNode root, int sum) {
        if(root == null) return 0;
        // dfs로 합계값을 확인
        dfs(root, sum, 0);
        // 이 함수를 왼쪽리프노드에서부터 다시 실행
        pathSum(root.left, sum);
        // 이 함수를 오른쪽 리프노드에서부터 다시 실행행
        pathSum(root.right, sum);
        return total;
    }

    void dfs(TreeNode root, int sum, long curr) {
        if(root == null) return;
        curr += root.val;
        if(curr == sum) total++;
        dfs(root.left, sum, curr);
        dfs(root.right, sum, curr);
    }
}
```