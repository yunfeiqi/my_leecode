
# 双指针方法 window [left right ]

import sys

# 双指针 left right
'''
right
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
left 
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # defination
        n = len(nums)
        left = 0
        right = 0
        window = sys.maxsize

        # terminator
        if n == 0:
            return 0

        # process
        sam_val = 0
        while right < n:
            # move right pointer
            sam_val += nums[right]
            right += 1

            # move left pointer
            while sam_val >= s:
                # min windows size
                window = min((right - left), window)
                sam_val = sam_val - nums[left]
                left += 1

        # return min value
        return 0 if window == sys.maxsize else window
