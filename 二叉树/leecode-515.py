# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 基于广度优先-使用队列
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        # defination
        result = []
        from queue import Queue
        m_queue = Queue()
        m_queue.put(root)

        # terminator
        if root is None:
            return result

        # process
        while m_queue.qsize() > 0:
            _cnt = m_queue.qsize()

            max_val = float("-inf")
            for i in range(_cnt):
                node = m_queue.get()
                if node.val > max_val:
                    max_val = node.val
                if node.left is not None:
                    m_queue.put(node.left)

                if node.right is not None:
                    m_queue.put(node.right)
            result.append(max_val)

        # return
        return result


# 基于广度优先-使用堆栈
class Solution2:
    def largestValues(self, root: TreeNode) -> List[int]:
        # defination
        result = []
        stack = []
        stack.append(root)

        # terminator
        if root is None:
            return result

        # process
        while stack:
            _cnt = len(stack)
            max_val = float("-inf")
            for i in range(_cnt):
                node = stack.pop()
                if node.val > max_val:
                    max_val = node.val
                if node.left is not None:
                    stack.insert(0, node.left)

                if node.right is not None:
                    stack.insert(0, node.right)

            result.append(max_val)

        # return
        return result


# 基于深度优先
class Solution3:
    def largestValues(self, root: TreeNode) -> List[int]:
        # defination
        result = []

        def level(root, n_level):
            if len(result) == n_level:
                result.append(float("-inf"))
            if root.val > result[n_level]:
                result[n_level] = root.val

            if root.left is not None:
                level(root.left, n_level + 1)

            if root.right is not None:
                level(root.right, n_level + 1)

        # terminator
        if root is None:
            return result

        # process
        level(root, 0)

        # return
        return result
