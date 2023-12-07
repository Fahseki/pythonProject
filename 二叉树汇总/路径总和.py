# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        num = 0
        num += root.val

        # 先写结束条件：如果走到了最后一个节点，当前路径所有节点值加起来是否等于目标值
        if root.left is None and root.right is None:
            if num == targetSum:
                return True
            else:
                return False

        # 循环执行：左节点为空就递归调用右节点，继续往下面找路径
        if root.left is None:
            return self.hasPathSum(root.right, targetSum - num)
        if root.right is None:
            return self.hasPathSum(root.left, targetSum - num)

        # 两条路的话，就递归调用两边的子节点
        return self.hasPathSum(root.left, targetSum - num) or self.hasPathSum(root.right, targetSum - num)

