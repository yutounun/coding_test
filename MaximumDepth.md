# 目的
かなり備忘録。ちょっと再帰関数あたり自分の考えを無理やり文字にしたような形でわかりづらいかと思うがご了承いただきたい。
[「1389. Create Target Array in the Given Order」](https://leetcode.com/problems/create-target-array-in-the-given-order/)などのノードだとかツリーとかが出てこない問題は絶対クリアできるとまではいかないが、少なくとも解説見れば理解できた。

だが、このNodeTreeなどは何をどのように実装しているのかが全く理解できず長らくクリアできず解説も訳がわからなかった。
しかし、今ちゃんと理解できたのでこちらに記載する。


# problem
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

![スクリーンショット 2022-02-13 午前11.13.14.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/487834/05f090ba-5d6f-1554-eae7-3b977e650e1f.png)


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

# 前提
問題の中の関数の引数でrootが渡されていて、exampleのrootを見るとrootはリスト??と思ったが、これが全ての間違いの始まりだった。
rootとして何を受け取っているのか中身を見てみた。

"**TREENODE IS NOT JUST A LIST!!**"

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

ツリーそのものがrootという引数に入っていて、listなどでは全くなかった。
solutionで出てくるroot.leftなどは上の中身を見ると想像がつきやすいと思う。

# solution
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))  
        else:
            return 0
```

再帰関数で一回再帰するごとに一個深い層を見ている

1. rootは左右両方あるからreturn1
2. rootはleft1。left1にはleft,rightがないから０が返って```self.maxDepth(root.left), self.maxDepth(root.right)```は0
3. rootはright1。right１層目はleft2層目もright2層目もあるから1が返る(```self.maxDepth(root.left), self.maxDepth(root.right)```は1)
4. rightの下のleft2層目はleft,rightがないから０を返す(```self.maxDepth(root.left), self.maxDepth(root.right)```は0)
5. rightの下のright2層目はleft,rightがないから０を返す(```self.maxDepth(root.left, self.maxDepth(root.right))```は0)

ちょっとわかりづらいかもしれないが、単純な再帰関数。

# まとめ

かなりスッキリしました。
もう一度実装してみたいと思う。
