# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗二叉树。


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(inorder_left, inorder_right, postorder_left, postorder_right):
            if inorder_left > inorder_right:
                return None

            # 后序遍历中的最后一个，就是根节点
            postorder_root = postorder_right

            # 拿已知的根节点的值，去哈希表中找到其在中序遍历中的指针位置
            inorder_root = index[postorder[postorder_root]]

            # 开始构造二叉树，根节点是当前的这个root
            root = TreeNode(postorder[postorder_root])

            # 得到左子树的节点个数 = 中序遍历中，root左边的个数
            size_left = inorder_root - inorder_left

            # 开始递归左子树，中序序遍历中，左子树的起始位置= 最左边, 终点位置= root - 1；
            #              后序序遍历中，左子树的起始位置= 最左边, 终点位置= 最左边 右移节点个数 左移1
            root.left = build(inorder_left, inorder_root-1, postorder_left, postorder_left+ size_left-1)

            # 开始递归右子树，中序遍历中，右子树的起始位置= 根节点+1, 终点位置= 最右边
            #              后序遍历中，右子树的起始位置= 最左边 + 节点个数, 终点位置= 根节点-1
            root.right = build(inorder_root+1, inorder_right, postorder_left+size_left, postorder_root-1)

            return root

        n = len(inorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return build(0, n-1, 0, n-1)
