"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# 采用层序遍历方法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # defination
        stack = []
        stack = [root]

        # terminator
        if root is None:
            return root

        # process

        while stack:
            _cnt = len(stack)
            pre = None
            for i in range(_cnt):
                node = stack.pop()
                node.next = pre
                pre = node

                if node.right is not None:
                    stack.insert(0, node.right)

                if node.left is not None:
                    stack.insert(0, node.left)
        # return
        return root


# 采用层序遍历方法
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        # defination
        cur = root

        # terminator
        if root is None:
            return root

        # process
        while cur is not None:
            # dummy node that represent sub level node for current node
            head = Node(0)
            pre = head
            # access all nodes with current level
            while cur is not None:
                if cur.left is not None:
                    pre.next = cur.left
                    # update previous node
                    pre = cur.left

                if cur.right is not None:
                    pre.next = cur.right
                    # update previous node
                    pre = cur.right

                # shift node to right
                cur = cur.next
            # shift to the most left node of next level
            cur = head.next
        # return
        return root
