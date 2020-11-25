# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 采用递归方式
# setp1: Find max value
# step2: create node with max value
# step3: create left sub-tree for node of current leval
# step4: create right sub-tree for node of current level
# step5: terminator condition: left == right
class Solution:

    # find index of max value which in specific range
    def max_value(self, nums, left, right):
        max_v = nums[left]
        max_idx = left
        for idx in range(left+1, right):
            if nums[idx] > max_v:
                max_idx = idx
                max_v = nums[idx]

        return max_idx, max_v

    # connect tree
    def connect(self, nums, left, right):

        # terminator
        if left == right:
            return None

        idx, max_val = self.max_value(nums, left, right)
        node = TreeNode(max_val)

        node.left = self.connect(nums, left, idx)
        node.right = self.connect(nums, idx+1, right)

        # terminator
        return node

    # main function
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # defination
        node = None

        # terminator
        if len(nums) <= 0:
            return node

        # process
        node = self.connect(nums, 0, len(nums))

        # return
        return node
