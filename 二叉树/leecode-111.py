# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 基于递归DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # defination

        # terminator
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        # process
        min_depth = float("inf")
        if root.left is not None:
            min_depth = min(self.minDepth(root.left), min_depth)

        if root.right is not None:
            min_depth = min(self.minDepth(root.right), min_depth)

        # return
        return min_depth + 1


# 基于BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # defination
        level = 0
        stack = []
        stack.append(root)

        # terminator
        if root is None:
            return 0

        # process
        while stack:
            _cnt = len(stack)
            level += 1
            for i in range(_cnt):
                node = stack.pop()
                # terminator
                if node.left is None and node.right is None:
                    return level

                # add node
                if node.left is not None:
                    stack.insert(0, node.left)
                if node.right is not None:
                    stack.insert(0, node.right)

        # return


# 基于BFS- 使用队列
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # defination
        level = 0
        from queue import Queue
        m_queue = Queue()
        m_queue.put(root)

        # terminator
        if root is None:
            return 0

        # process
        while m_queue.qsize() > 0:
            _cnt = m_queue.qsize()
            level += 1
            for i in range(_cnt):
                node = m_queue.get()
                # terminator
                if node.left is None and node.right is None:
                    return level

                # add node
                if node.left is not None:
                    m_queue.put(node.left)
                if node.right is not None:
                    m_queue.put(node.right)

        # return
