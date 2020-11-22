## python 刷题常用的数据结构定义

```python
# 最大值
sys.maxint
# 最小值
-sys.maxint -1
# 双端队列，看成栈或者队列
queue = collections.dequeue([1])
queue.popleft() 出队
queue.pop() 出栈
queue.append() 入队、栈
queue[0] 队首
queue[-1]栈顶
# 二叉树
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```