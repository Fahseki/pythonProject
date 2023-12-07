# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历， inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            # 先序遍历中的第一个，就是根节点
            preorder_root = preorder_left

            # 拿已知的根节点的值，去哈希表中找到其在中序遍历中的指针位置
            inorder_root = index[preorder[preorder_root]]

            # 开始构造二叉树，根节点是当前的这个root
            root = TreeNode(preorder[preorder_root])

            # 得到左子树的节点个数 = 中序遍历中，root左边的个数
            size_left = inorder_root - inorder_left

            # 开始递归左子树，先序遍历中，左子树的起始位置= root/left+1, 终点位置= root/left + 节点个数；
            #              中序遍历中，左子树的起始位置= 中序起点, 终点位置= 中序中root-1
            root.left = build(preorder_left+1, preorder_left + size_left, inorder_left, inorder_root-1)

            # 开始递归右子树，先序遍历中，右子树的起始位置= 从最左边开始+1+左子树个数, 终点位置= 最右边
            #              中序遍历中，右子树的起始位置= root+1, 终点位置= 最右边
            root.right = build(preorder_left+size_left+1, preorder_right, inorder_root+1, inorder_right)

            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return build(0, n-1, 0, n-1)
