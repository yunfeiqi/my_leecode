# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 基于递归
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        # termiantor
        if root is None or root.val == val:
            return root

        # process
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# 基于递归
class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        # termiantor
        if root is None:
            return root

        # process
        while (root is not None and root.val != val):
            if val < root.val:
                root = root.left
            else:
                root = root.right

        return root
