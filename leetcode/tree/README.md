[toc]
#### 二叉树的遍历

```python
def dfs(root):
    if not root:
        return
    # 前序遍历
    self.dfs(root.left)
    # 中序遍历
    self.dfs(root.right)
    # 后续遍历
```
#### 递归的理解

> 树的递归可以理解为先把当前节点压栈，处理完之后再回过头来处理该节点。

#### 自顶向下（前序）
> 前序遍历可以看成自顶向下的思考方式，先对当前根的节点的值进行处理，然后再处理左右节点。

```python
def dfs(root, some_val):
    if not root:
        return 0
    # 计当前根节点的一些数据并且带入左右子树继续计算
    some_val = root.val
    left = self.dfs(root.left, some_val)
    right = self.dfs(root.right, some_val)
    return xx
```

Example - 自顶向下
```python
# 二叉树所有路径
def travel(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            if path:
                path += "->" + str(root.val)
            else:
                path = str(root.val)
            self.path_lst.append(path)
            return
        if path:
            path += "->" + str(root.val)
        else:
            path = str(root.val)
        self.travel(root.left, path)
        self.travel(root.right, path)
# 左叶子之和， 记录父节点
def travel(self, node, parent):
        if node:
            if parent:
                if not node.right and not node.left and parent.left == node:
                    self.lst.append(node.val)
            self.travel(node.left, node)
            self.travel(node.right, node)
```

####自底向上（后序）
>后序遍历可以看成自底向上的思考方式，先假设左右节点已经得到正确的值，然后回溯到根节点进行处理。

```python
def dfs(root):
    if not root:
        return 0
    # 和return部分呼应
    left = self.dfs(root.left)
    right = self.dfs(root.right)
    # 借助于回溯的特性，计算依赖于子节点属性的根节点的一些值
    xx
    xx
    xx
    # 返回值与该dfs函数的作用相关，比如求当前节点所有子树之和、当前的节点的深度等，需要和
    return xx
```
Example - 自底向上
```python
# 公共祖先
 def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        # 在root节点下 p q 的公共祖先
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if right:
            return right
        if left:
            return left
        return None
# 深度
def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
# 合并二叉树
def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        node = None
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            node = t1
            node.left = self.mergeTrees(t1.left, None)
            node.right = self.mergeTrees(t1.right, None)
        elif t2:
            node = t2
            node.left = self.mergeTrees(None, t2.left)
            node.right = self.mergeTrees(None, t2.right)
        return node
```

#### 二叉排序树（中序）
> 中序遍历的主要作用是在于二叉搜索树的一些问题，因为中序遍历二叉搜索树的时候，是一个升序的序列，只要提到二叉搜索树，就会想到如何中序遍历。

```python
1、二叉搜索树前置节点的记录
2、dummpy节点
# 二叉搜索树中的众数
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre_val = None
        self.result = []
        self.max_times = 0
        self.cur_times = 0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.travel(root)
        return self.result

    def travel(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return
        self.travel(root.left)
        if self.pre_val is None:
            self.result = [root.val]
            self.max_times = 1
            self.cur_times = 1
        else:
            if root.val == self.pre_val:
                self.cur_times += 1
            else:
                self.cur_times = 1
            if self.cur_times > self.max_times:
                self.result = [root.val]
                self.max_times = self.cur_times
            elif self.cur_times == self.max_times:
                self.result.append(root.val)
        self.pre_val = root.val
        self.travel(root.right)
```



#### 二叉树、对称（翻转）、镜像、相同、问题
>两个二叉树可以做是否对称的判断，当需要对一个二叉树进行判断比较的时候，需要看成两棵树，这样分别看左右子树就行。

```python
#翻转 or 镜像
root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#对称
def compare(self, left, right):
        if not left and not right:
            return True
        if left and right:
            return left.val == right.val and self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else:
            return False
# 相同
 def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
```
