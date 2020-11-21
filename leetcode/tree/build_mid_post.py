#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: build_mid_post.py
@time: 2020/11/14 16:51
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义以及中序遍历
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root = self.build(0, len(inorder) - 1, postorder, inorder)
        return root

    def build(self, left, right, root_list, inorder):
        """
        递归建立二叉树，先递归右子树的原因是二叉树后序遍历，先左后右，所有优先得到是右子树的根和节点
        :param left:
        :param right:
        :param root_list:
        :param inorder:
        :return:
        """
        if left > right:
            return
        root_val = root_list.pop()
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        root.right = self.build(index + 1, right, root_list, inorder)
        root.left = self.build(left, index - 1, root_list, inorder)
        return root
