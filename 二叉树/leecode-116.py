"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 基于广度优先--使用堆栈


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # defination
        stack = []
        stack.append(root)

        # terminator
        if root is None:
            return root

        # process
        while stack:
            _cnt = len(stack)

            pre_node = None
            for i in range(_cnt):
                node = stack.pop()
                node.next = pre_node
                pre_node = node

                if node.right is not None:
                    stack.insert(0, node.right)
                if node.left is not None:
                    stack.insert(0, node.left)

        # return
        return root


# 使用现有指针完成
# Step 1 : pre.next = current.right : 完成同父指向
# Step 2 : pre = pre.next  ： 完成兄弟转移
# Step 3: cur = cur.next :  完成父亲转换
# Step 4: pre.next = cur.left: 完成表亲连接
# Step 5: pre = pre.next : 完成兄弟转移
# Step 6: pre.next = cur.right: 完成一次迭代
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        # defination
        # 链表最左侧，层级表示
        level = root
        cur = None

        # terminator
        if root is None:
            return root

        # process
        # 第一层不需要建立，本来就是 None,从第二层着手处理
        # 处理所有层
        while level.left is not None:
            # cur 当前层处理节点（为子孙某福利的父亲）
            cur = level

            # 如果cur 不是None 说明当前层没有遍历完
            while cur:
                # Step1 ：同父兄弟指针
                cur.left.next = cur.right

                # step2: 异父表亲指针(前提是存在叔伯)
                if cur.next is not None:
                    cur.right.next = cur.next.left

                # step 3: 同层转移
                cur = cur.next

            # 当前层更新完毕，更换下一层
            level = level.left
        # return
        return root

# 基于DFS，采用指针方式完成


class Solution3:
    def connect(self, root: 'Node') -> 'Node':
        # defination
        def dfs(current, cur_next):
            # termiantor
            if current is None:
                return

            # step 1 : 当前节点指针
            current.next = cur_next

            # 同父兄弟指针
            dfs(current.left, current.right)

            # 异父表亲指针(有表亲)
            if current.next is not None:
                dfs(current.right, current.next.left)
            else:
                dfs(current.right, None)

        # terminator
        if root is None:
            return root

        # process
        dfs(root, None)

        # return
        return root
