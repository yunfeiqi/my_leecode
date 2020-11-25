# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 基于广度优先迭代方法-基于Queue

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # defination
        result = []
        from queue import Queue
        q_node = Queue()
        q_node.put(root)

        # terminator
        if root is None:
            return result

        # for loop
        while q_node.qsize() > 0:
            _len = q_node.qsize()
            _tmp_res = []
            for i in range(_len):
                node = q_node.get()
                _tmp_res.append(node.val)
                if node.left is not None:
                    q_node.put(node.left)
                if node.right is not None:
                    q_node.put(node.right)
            result.append(_tmp_res)
        # return
        result.reverse()
        return result


# 基于迭代方法-
class Solution2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # defination
        result = []
        stack = []
        stack.append(root)

        # terminator
        if root is None:
            return result

        while stack:
            _len = len(stack)
            _tmp_res = []
            for i in range(_len):
                node = stack.pop()
                _tmp_res.append(node.val)

                if node.left is not None:
                    stack.insert(0, node.left)
                if node.right is not None:
                    stack.insert(0, node.right)

            # append current lavel result
            result.append(_tmp_res)

        # reverse result
        result.reverse()
        return result


# 基于DFS
class Solution3:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        # defination
        result = []

        def level(root, n_level):
            if root is None:
                return

            if len(result) == n_level:
                result.append([])

            result[n_level].append(root.val)

            if root.left is not None:
                level(root.left, n_level + 1)
            if root.right is not None:
                level(root.right, n_level + 1)

        # terminator

        if root is None:
            return result

        # loop
        level(root, 0)

        # return
        result.reverse()
        return result
