# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 基于广度优先--队列
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # defination
        result = []
        from queue import Queue
        q_node = Queue()
        q_node.put(root)

        # terminator
        if root is None:
            return result

        # process
        while q_node.qsize() > 0:
            _cnt = q_node.qsize()

            for i in range(_cnt):
                node = q_node.get()

                # add node value from right view
                if i == _cnt-1:
                    result.append(node.val)

                if node.left is not None:
                    q_node.put(node.left)

                if node.right is not None:
                    q_node.put(node.right)

        # return
        return result


# 基于广度优先--堆栈
class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:

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
            for i in range(_cnt):
                node = stack.pop()
                if i == 0:
                    result.append(node.val)

                if node.right is not None:
                    stack.insert(0, node.right)

                if node.left is not None:
                    stack.insert(0, node.left)

        # return
        return result


# 基于DFS
class Solution3:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # defination
        result = []

        def level(root, n_level, add=False):
            if root is None:
                return

            if len(result) == n_level and add:
                result.append(root.val)

            _tmp_status = True
            if root.right is not None:
                level(root.right, n_level+1, True)
                _tmp_status = False

            if root.left is not None:
                level(root.left, n_level+1, _tmp_status)

        # terminator
        if root is None:
            return result

        # process
        level(root, 0, True)
        # return
        return result
