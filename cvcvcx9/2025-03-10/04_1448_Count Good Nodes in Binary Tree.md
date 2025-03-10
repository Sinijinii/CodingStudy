```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // 굿노드는 루트노드에서부터 자기까지이르는 순회에서 자기 자신이 가장 큰 값일 때 굿노드
    public int goodNodes(TreeNode root) {
        if(root == null) return 0;
        return dfs(root,root.val);
    }
    // dfs로 그래프를 순회하면서 최대값과 비교하여 노드의 값이 가장 클 때, 확인인
    private int dfs(TreeNode root, int max){

        if(root == null){
            return 0;
        }

        max = Math.max(root.val,max);

        if(root.val >= max){
            return 1 + dfs(root.left,max) + dfs(root.right,max);
        }else{
            return dfs(root.left, max) + dfs(root.right, max);
        }
    }
}
```