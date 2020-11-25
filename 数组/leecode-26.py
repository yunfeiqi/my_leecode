'''
数组左移动，
left_idx 记录了新数组长度
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # defination
        left_idx = 0
        num_len = len(nums)

        # process
        # 没有或者只有1项时直接返回
        if num_len <= 1:
            return num_len

        # 从1开始遍历
        for pre_idx in range(1, num_len):
            # idx shift to right

            # 不等，则赋值
            if nums[left_idx] != nums[pre_idx]:
                left_idx += 1
                nums[left_idx] = nums[pre_idx]

        # return
        return left_idx + 1
