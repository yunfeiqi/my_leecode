# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Left Right Root
class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def postorder(root: TreeNode):
            if root is None:
                return

            postorder(root.left)
            postorder(root.right)
            result.append(root.val)

        postorder(root)
        return result


'''
@Desc    :   Post Order by Stack
        1. 拿到每个节点，并把节点入栈，
        2. 如果当前节点有左子树，则继续遍历左子树
        3. 栈内容出栈
        3. 同样方式遍历右子树
@Time    :   2020/09/29 13:19:56
@Author  :   sam.qi 
'''


class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        # defination
        stack = []
        prev = None
        result = []

        # terminator
        if root is None:
            return []

        # condition for while
        while root or stack:
            # left tree pushed to stack
            while root:
                stack.append(root)
                root = root.left

            # pop leaf node
            root = stack.pop()

            # is has right node or the right node has beed accessed
            if root.right is None or root.right == prev:
                result.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return result


# 后序遍历，Left Right Root ，其实和前序遍历右关系 Root Left Right，
# 只要把 前序变成 Root Right Left 在反转就是后序遍历
# 推荐方式
class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # defination
        stack = [root]
        result = []

        if root is None:
            return []

        while stack:
            root = stack.pop()
            if root is not None:
                result.append(root.val)
                stack.append(root.left)
                stack.append(root.right)

        result.reverse()
        return result
