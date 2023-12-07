# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 遍历完了，节点都是空
        if p is None and q is None:
            return True
        # 节点一个为空一个不为空
        if p is None or q is None:
            return False
        # 节点不一样
        if p.val != q.val:
            return False
        # 当前节点一样，递归调用，比较左节点和右节点
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
