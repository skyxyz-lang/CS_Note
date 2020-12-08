#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: tree.py
@time: 2020/12/5 22:16
@source:
@desc:
"""


# N叉树定义
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 二叉树定义
class TreeNode(object):

     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):

    def __init__(self):
        self.parent_map = {}
        self.depth_map = {}

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.build_tree_bst(nums, 0, len(nums) -1 )
        return root

    def build_tree_bst(self, nums, left, right):
        """

        :param nums:
        :param left:
        :param right:
        :return:
        """
        if left > right:
            return None
        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        root.left = self.build_tree_bst(nums, left, mid - 1)
        root.right = self.build_tree_bst(nums, mid + 1, right)
        return root

    def mirrorTree(self, root):
        """
        二叉树的镜像/翻转
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        left = self.mirrorTree(root.right)
        right = self.mirrorTree(root.left)
        root.left = left
        root.right = right
        return root

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if not root:
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root

    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth2(root.left)
        right = self.maxDepth2(root.right)
        return max(left, right) + 1

    def maxDepth(self, root):
        """
        N叉树的最大深度
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        lst = []
        for ch in root.children:
            lst.append(self.maxDepth(ch))
        return max(lst) + 1 if lst else 1

    def lowestCommonAncestor(self, root, p, q):
        """
        二叉树的最近公共祖先
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        return None

    def lowestCommonAncestorBST(self, root, p, q):
        """
        二叉搜索树的最近公共祖先
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def isSymmetric(self, root):
        """
        是否对称
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        """

        :param left:
        :param right:
        :return:
        """
        if left and right:
            return left.val == right.val and self.compare(left.right, right.left) and self.compare(left.left, right.right)
        elif not left and not right:
            return True
        return False

    def isBalanced(self, root):
        """
        是否平衡
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isSubtree(self, s, t):
        """
        子树判断
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and t:
            return False
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t):
        """

        :param s:
        :param t:
        :return:
        """
        if not s and not t:
            return True
        elif s and t:
            return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        else:
            return False

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.travel(root, None)
        return self.depth_map.get(x, -1) == self.depth_map.get(y, -2) and self.parent_map.get(x) != self.parent_map.get(y)

    def travel(self, node, parent):
        """

        :param node:
        :param parent:
        :return:
        """
        if node:
            if not parent:
                self.depth_map[node.val] = 1
            else:
                self.depth_map[node.val] = self.depth_map[parent.val] + 1
                self.parent_map[node.val] = parent.val
        self.travel(node.left, node)
        self.travel(node.right, node)

    def quick_sort(self, arr, left, right):
        """

        :param arr:
        :param left:
        :param right:
        :return:
        """
        l = left
        r = right
        if left > right:
            return
        point = arr[left]
        while left < right:
            while left < right and arr[right] >= point:
                right -= 1
            if left < right:
                arr[left] = arr[right]
                left += 1
            while left < right and arr[left] < point:
                left += 1
            if left < right:
                arr[right] = arr[left]
                right -= 1
        arr[left] = point
        self.quick_sort(arr, l, left -1 )
        self.quick_sort(arr, left + 1, r)
        return arr
