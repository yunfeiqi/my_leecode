# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BaseLine
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # defination
        num_node = 0

        # terminator
        if root is None:
            return num_node

        # process
        num_node = 1 + self.countNodes(root.left) + self.countNodes(root.right)

        # return
        return num_node


# 利用二叉树特性，满二叉树节点数为 2**d -1 ,d 表示树深度
class Solution2:

    def depth(self, root):
        depth = 0
        if root is None:
            return 0

        while root is not None:
            root = root.left
            depth += 1

        return depth

    def exist(self, idx, d, root):
        # defination
        left = 0
        right = (2**d - 1) - 1

        # terminator

        # process
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                root = root.left
                right = pivot
            else:
                root = root.right
                left = pivot + 1

        # return
        return not root is None

    def countNodes(self, root: TreeNode) -> int:
        # defination
        num_nodes = 0

        # terminator
        if root is None:
            return num_nodes

        # process
        d = self.depth(root)
        # number node of fully binary tree
        num_nodes = 2**d - 1
        # check each leaf node is exist
        idxs = list(range(2**(d-1)-1, -1, -1))
        leak_num = 0
        for idx in idxs:
            if self.exist(idx, d-1, root):
                break
            leak_num += 1

        num_nodes = num_nodes - leak_num

        # return
        return num_nodes


# 利用二叉树特性，两次二分法
class Solution3:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left
