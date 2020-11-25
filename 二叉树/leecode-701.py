# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 前提新值和二叉树任意值不重复


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # defination
        cur = root

        # terminator
        if root is None:
            return TreeNode(val)

        # process
        while True:
            if val < cur.val:
                if cur.left is None:
                    node = TreeNode(val)
                    cur.left = node
                    break
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    node = TreeNode(val)
                    cur.right = node
                    break
                else:
                    cur = cur.right

        # return
        return root


class Solution2:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # terminator
        if root is None:
            return TreeNode(val)

        # Left Insert
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Right Insert
            root.right = self.insertIntoBST(root.right, val)

        # return
        return root
