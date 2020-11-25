# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历-递归
class Solution:

    pre_val = float("-inf")

    def isValidBST(self, root: TreeNode) -> bool:
        # defination

        def check(root):
            # terminator
            if root is None:
                return True

            if not check(root.left):
                return False

            if root.val <= self.pre_val:
                return False

            self.pre_val = root.val

            if not check(root.right):
                return False

            return True

        # terminator
        if root is None:
            return True

        # process
        return check(root)


# 中序遍历-迭代
class Solution2:

    def isValidBST(self, root: TreeNode) -> bool:
        # defination
        result = True
        stack = []
        pre_val = float("-inf")

        # terminator
        if root is None:
            return True

        # process
        while root or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val <= pre_val:
                    result = False
                    break
                pre_val = root.val
                root = root.right

        # return
        return result
