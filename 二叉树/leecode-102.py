# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

# 基于广度优先迭代方法-基于Queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # defination
        from queue import Queue
        result = []
        mqueue = Queue()
        mqueue.put(root)

        if root is None:
            return result

        # while condition
        while mqueue.qsize() > 0:
            # current leval count
            n_cnt = mqueue.qsize()
            current_res = []
            for i in range(n_cnt):
                # pop all node with current level
                root = mqueue.get()
                current_res.append(root.val)
                if root.left is not None:
                    mqueue.put(root.left)
                if root.right is not None:
                    mqueue.put(root.right)
            if len(current_res) > 0:
                result.append(current_res)
        return result


# 基于广度优先迭代方法-基于 Stack
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # defination
        result = []
        # 维护了广度优先节点
        stack = [root]

        if root is None:
            return result

        # while condition
        while stack:
            # current leval count
            n_cnt = len(stack)
            current_res = []
            for i in range(n_cnt):
                # pop all node with current level
                root = stack.pop()
                current_res.append(root.val)
                if root.left is not None:
                    # 插入到栈低
                    stack.insert(0, root.left)
                if root.right is not None:
                    # 插入到栈底，把堆栈拉长
                    stack.insert(0, root.right)
            if len(current_res) > 0:
                result.append(current_res)
        return result


# 基于深度优先递归
class Solution3:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # defination
        result = []

        # terminator
        if root is None:
            return result

        def level(root, level_n):
            if root is None:
                return
            if len(result) == level_n:
                result.append([])
            result[level_n].append(root.val)

            if root.left is not None:
                level(root.left, level_n + 1)
            if root.right is not None:
                level(root.right, level_n + 1)

        # processing
        level(root, 0)

        # return
        return result


'''
@Desc    :   DFS
@Time    :   2020/10/01 11:13:45
@Author  :   sam.qi 
'''


def dfs(root: TreeNode):
    if root is None:
        return
    if root.left is not None:
        dfs(root.left)
    if root.right is not None:
        dfs(root.right)


def bfs(root: TreeNode):
    # defination
    stack = []

    # edge condition
    if root is None:
        return

    stack.append(root)
    while stack:
        root = stack.pop()
        if root.left is not None:
            stack.insert(0, root.left)
        if root.right is not None:
            stack.insert(0, root.right)
