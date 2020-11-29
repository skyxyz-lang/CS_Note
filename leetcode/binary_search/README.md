### 二分查找
1、经典版本，主要是在一个已经排序的数组里查找数据是否存在。
```python
    def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) / 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
```
2、有序数据边界寻找，分别分为左边界和右边界，理解的时候可以把target看成不存在在当前有序数据A之中
>2.1、左边界是指对于一个有序数组A，寻找第一个可以插入元素的位置，或者说寻找第一个大于等于target元素的位置
例如：a = [1, 1, 1, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10] target = 2
左边界是指 3
```python
    def left_bound(nums, target):
        """

        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1

        if left >= len(nums):
            return -1
        return left
```
>2.2、右边界是指对于一个有序数组A，寻找第一个小于等于target元素的位置
例如：a = [1, 1, 1, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10] target = 2
最右边的3为index=2
```python
    def right_bound(nums, target):
        """

        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1
        if right < 0:
            return -1
        return right
```
