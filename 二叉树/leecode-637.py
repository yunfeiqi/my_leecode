# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 采用广度优先-基于Queue
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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

            _sum = 0
            for i in range(_cnt):
                node = m_queue.get()
                _sum += node.val

                if node.left is not None:
                    m_queue.put(node.left)
                if node.right is not None:
                    m_queue.put(node.right)

            result.append(_sum / _cnt)

        # return
        return result


# 采用广度优先-基于堆栈
class Solution2:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
            _sum = 0
            for i in range(_cnt):
                node = stack.pop()
                _sum += node.val
                if node.left is not None:
                    stack.insert(0, node.left)
                if node.right is not None:
                    stack.insert(0, node.right)
            result.append(_sum / _cnt)

        # return
        return result


# 采用深度优先
class Solution3:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # defination
        result = []
        l_sum = []
        l_num = []
        level_num = []

        def level(root, n_level):
            if root is None:
                return
            if len(l_sum) == n_level:
                l_sum.append(0)
                l_num.append(0)

            l_sum[n_level] += root.val
            l_num[n_level] += 1

            if root.left is not None:
                level(root.left, n_level + 1)

            if root.right is not None:
                level(root.right, n_level + 1)

        # terminator
        if root is None:
            return result

        # process
        level(root, 0)
        result = [i_sum/i_num for i_sum, i_num in zip(l_sum, l_num)]
        # return
        return result
