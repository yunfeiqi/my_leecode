# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Root Left Right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        # defination
        result = []

        # define recursive function
        def preorder(root: TreeNode):
            if root is None:
                return

            result.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return result


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        # defination
        stack = [root]
        result = []

        # terminator
        if root is None:
            return []

        while stack:
            root = stack.pop()
            if root is not None:
                result.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return result
