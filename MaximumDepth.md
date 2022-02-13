# problem
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

Example 2:

```
Input: root = [1,null,2]
Output: 2
``` 

Constraints:

```
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
```
# solution
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))  
        else 
            return 0:
```

再帰関数で一回再帰するごとに一個深い層を見ている

1. rootは左右両方あるからreturn1
2. left1にはleft,rightがないから０が返って```self.maxDepth(root.left), self.maxDepth(root.right)```は0
3. right１層目はleft2層目もright2層目もあるから1が返る(```self.maxDepth(root.left), self.maxDepth(root.right)```は1)
4. rightの下のleft2層目はleft,rightがないから０を返す(```self.maxDepth(root.left), self.maxDepth(root.right)```は0)
5. rightの下のright2層目はleft,rightがないから０を返す(```self.maxDepth(root.left, self.maxDepth(root.right))```は0)


# tips

What's in the TreeNode is following

It means "**TREENODE IS NOT JUST A LIST!!**"

```json
TreeNode{
  // root node(depth = 1)
  val: 3, 
  // left side of the tree
  left: TreeNode{
    // depth = 1
    val: 9, 
    left: None, 
    right: None
  }, 
  // right side of the tree
  right: TreeNode{
    // depth = 2
    val: 20, 
    left: TreeNode{
      // depth = 3
      val: 15, 
      left: None, 
      right: None}, 
    right: TreeNode{
      // depth = 3
      val: 7, 
      left: None, 
      right: None}
  }
}
```
