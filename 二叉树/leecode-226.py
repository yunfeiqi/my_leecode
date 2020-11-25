# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 基于递归的方法-DFS
# left  = right , right = left
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # defination

        # terminator
        if root is None:
            return root

        # process
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        # return
        return root


# 基于迭代的方法-BFS
# left  = right , right = left
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # defination
        stack = []
        stack.append(root)

        # terminator
        if root is None:
            return root

        # process
        while stack:
            node = stack.pop()
            # shift children's position
            node.left, node.right = node.right, node.left

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)

        # return
        return root
