# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 如果要删除的节点是叶子节点，我们直接删除即可。

# 如果删除的结点不是叶子节点，并且有一个子节点为空，我们直接返回另一个不为空的子节点即可。

# 如果删除的结点不是叶子节点，并且左右子树都不为空，我们可以用左子树的最大值替换掉要删除的节点或者用右子树的最小值替换掉要删除的节点都是可以的。


# 递归
class Solution:

    def finMax(self, node: TreeNode):
        while node.right is not None:
            node = node.right
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # defination

        # terminator
        if root is None:
            return None

        # process
        if key < root.val:
            # shift to left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            node = self.finMax(root.left)
            root.val = node.val
            root.left = self.deleteNode(root.left, root.val)

        # return
        return root
