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
    // 리프노드의 순서가 같은지 비교하는 메인함수
    // 여기에서 두 순서를 구한다.
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        var list1 = new ArrayList<Integer>();
        var list2 = new ArrayList<Integer>();

        dfs(list1,root1);
        dfs(list2,root2);

        if(list1.equals(list2)) return true;
        return false;

    }
    // dfs 그래프를 순회하면서 순서를 찾아봄
    // left와 right가 둘다 null인경우만 리스트에 추가하는 식으로 리프노트를 찾아냄
    private void dfs(List<Integer> list, TreeNode root){
        if(root==null) return;
        if(root.left == null && root.right== null){
            list.add(root.val);
            return;
        }else{
            dfs(list,root.left);
            dfs(list,root.right);
        }
    }
}
```