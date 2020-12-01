### 回溯法
1. 路径：也就是已经做出的选择。
2. 选择列表：也就是你当前可以做的选择。
3. 结束条件：也就是到达决策树底层，无法再做选择的条件。

```python
    # 排列是使用contains判断元素不重复使用，且有顺序
    # 组合问题使用start，组合内无顺序
    def backtrack(self, nums, start, cur_path):
        """
        
        :param nums:  nums 和 start 共同构成待选择列表
        :param start: 
        :param cur_path: 当前结果路径
        :return: 
        """
        if conditon is True:
            # 条件满足、收集结果, 常见组合、子集、排列 条件分别为到达叶子节点或者每一节点都收集
            self.final_result.append(cur_path)
            return 
        # 对于当前可选择的列表进行选择
        for i in range(start, len(nums)):
            # 进行选择
            cur_path.append(nums[i])
            # 进行回溯
            self.back_track(nums, i + 1, cur_path)
            # 撤销选择
            cur_path.pop()

```