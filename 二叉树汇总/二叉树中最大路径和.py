# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
class Solution(object):
    def __init__(self):
        self.total_num = -sys.maxsize - 1  # =float('-inf')  定义一个最小的数作为初始值

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxGain(node):

            if node is None:
                return 0

            # 找左右分别的最大路径值，如果子节点加起来小于零，那就当没有，不去经过
            left = max(0, maxGain(node.left))
            right = max(0, maxGain(node.right))

            # 更新一下当前的最大路径值
            self.total_num = max(self.total_num, node.val + left + right)

            # 返回必须经过当前这个节点后，最大的路径值
            return max(left, right) + node.val

        maxGain(root)
        return self.total_num
