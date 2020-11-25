# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # defination

        # process
        if t1 is None:
            return t2

        if t2 is None:
            return t1

        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        # return
        return t1


# BFS
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # defination
        stack = []
        stack.append(t2)
        stack.append(t1)

        # terminaton
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        # process
        while len(stack) > 0:
            left = stack.pop()
            right = stack.pop()

            left.val = left.val + right.val

            if left.left is not None and right.left is not None:
                stack.insert(0, left.left)
                stack.insert(0, right.left)

            if left.left is None:
                left.left = right.left

            if left.right is not None and right.right is not None:
                stack.insert(0, left.right)
                stack.insert(0, right.right)
            if left.right is None:
                left.right = right.right

        # return
        return t1
