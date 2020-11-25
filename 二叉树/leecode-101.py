# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 基于深度优先DFS-递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # defination
        result = False

        def dfs(left, right):
            # terminator
            # left and right are none
            if left is None and right is None:
                return True

            # one of biside is node
            if left is None or right is None:
                return False
            # the value of bose side node are not equal
            if left.val != right.val:
                return False

            # compare sub left node value of left and sub right node value of right
            # and sub right node value of left  and sub left node value of right
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        # terminator
        if root is None:
            return True

        # process
        result = dfs(root.left, root.right)

        # return
        return result


# 基于广度优先BFS-堆栈
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # defination
        stack = []

        # terminator
        if root is None:
            return True

        # process
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            # take paire node from stack
            l_node = stack.pop()
            r_node = stack.pop()

            # terminator
            if l_node is None and r_node is None:
                continue
            if l_node is None or r_node is None:
                return False
            if l_node.val != r_node.val:
                return False

            stack.insert(0, l_node.left)
            stack.insert(0, r_node.right)
            stack.insert(0, l_node.right)
            stack.insert(0, r_node.left)

        # return
        return True
