# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 基于递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # terminator
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1


# 基于-BFS
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        # defination
        depth = 0
        stack = []
        stack.append(root)

        # terminator
        if root is None:
            return depth

        # process
        while stack:
            _cnt = len(stack)
            for i in range(_cnt):
                node = stack.pop()
                if node.left is not None:
                    stack.insert(0, node.left)
                if node.right is not None:
                    stack.insert(0, node.right)

            depth += 1

        # return
        return depth


# 基于-DFS
class Solution3:
    def maxDepth(self, root: TreeNode) -> int:
        # defination
        stack = [0]

        def dfs(root, level):
            # terminator
            if root is None:
                return

            if root.left is not None:
                dfs(root.left, level + 1)
            if root.right is not None:
                dfs(root.right, level + 1)

            if stack[0] < level:
                stack[0] = level

        # terminator
        if root is None:
            return 0

        # process
        dfs(root, 0)

        # return
        return stack[0] + 1
