### 滑动窗口
解决的问题为
1. 子串排列包含问题
2. 子串覆盖问题


重点在于:
1. 滑动窗口的滑动区间是[left, right) 左闭右开
2. 首先滑动right指针更新一些状态
3. 更新完判断窗口是否需要收缩，并且在收缩的时候判是否存在解空间，如果存在进行更新结果
    1. 当前找到结果需要收缩，也就是滑动窗口找到最优解，收缩窗口进行优化解
    2. 当前没找到结果，但是由于条件限制如长度，需要收缩窗口

```python
def slide_window(self, s, t):
  
    need = dict()
    windows = dict()
    for c in t:
        self.add_dict_one(c, need)
    left = 0
    right = 0
    valid = 0
    start = 0
    length = sys.maxint
    # 右边进行滑动
    while right < len(s):
        c = s[right]
        right += 1
        self.add_dict_one(c, windows)
        # 判断当前window 和 need 是否满足
        if windows.get(c, 0) == need.get(c, -1):
            valid += 1
        # 窗口收缩的时间
        while valid == len(need):
            if (right - left) < length:
                length = right - left
                start = left
            d = s[left]
            left += 1
            if windows.get(d, 0) == need.get(d, -1):
                valid -= 1
            self.reduce_dict_one(d, windows)

```