"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# 基于广度优先-基于队列
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
            _nodes = []
            for i in range(_cnt):
                node = m_queue.get()
                _nodes.append(node.val)
                if node.children is not None:
                    for child in node.children:
                        if child is not None:
                            m_queue.put(child)
            result.append(_nodes)

        # return
        return result


# 基于广度优先-基于迭代
class Solution2:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
            _vals = []
            for i in range(_cnt):
                node = stack.pop()
                _vals.append(node.val)
                if node.children is not None:
                    for s_node in node.children:
                        if s_node is not None:
                            stack.insert(0, s_node)
            result.append(_vals)

        # return
        return result
