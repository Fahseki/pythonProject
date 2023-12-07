# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        list1 = [root]

        while list1:  # list1存放树节点，队列先入先出，先放根节点，出一个就放入两个子节点
            list2 = []
            i = 0
            numbers = len(list1)  # 储存每层的节点个数
            while i < numbers:
                list2.append(list1[0].val)  # 将一层的节点值打包成同一个列表
                if list1[0].left:  # 将本次要移出的节点，加入其两个子节点在队尾
                    list1.append(list1[0].left)
                if list1[0].right:
                    list1.append(list1[0].right)
                list1.pop(0)  # 最前面的节点移出队列
                i += 1
            res.append(list2[-1])  # 只保存每层的最后一个值
        return res
