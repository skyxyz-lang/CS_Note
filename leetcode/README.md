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
# 二维数据初始化
matrix = [[0 for i in range(3)] for j in range(3)]

# 数据切片
arr[0:mid]  获取 0, 1, 2, 3, ... mid - 1 的数据
arr[mid:]   获取 mid, 末尾全部的数据，区别于 arr[mid:-1]

```