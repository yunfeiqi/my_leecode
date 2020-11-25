
'''
url: https://mp.weixin.qq.com/s/Xytl05kX8LZZ1iWWqjMoHA
'''


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # defination
        pre_diff = 0
        curr_diff = 0
        num = 1
        size = len(nums)

        # terminator
        if size <= 1:
            return size

        # process
        for idx in range(1, size):
            curr_diff = nums[idx] - nums[idx-1]
            if (curr_diff > 0 and pre_diff <= 0) or (curr_diff < 0 and pre_diff >= 0):
                num += 1
                pre_diff = curr_diff
        # return

        return num
