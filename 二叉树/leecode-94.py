# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Left Root Right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # defination
        result = []

        # recursive function
        def inorder(root: TreeNode):
            # terminator
            if root is None:
                return

            # process and drill down
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # defination
        stack = []
        result = []

        # while condition
        while root or stack:
            # 当root和left 全部压入栈中，直到叶子节点
            if root:
                stack.append(root)
                root = root.left
            # 叶子节点，后就会访问ROOT
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
