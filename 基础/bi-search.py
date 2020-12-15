#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2020/12/14 19:44:49
@Author  :   sam.qi
@Version :   1.0
@Desc    :   二分查找法
'''


from typing import NoReturn


class Solution(object):

    def searchInsert(self, nums, target):

        # terminator
        if nums is None:
            return -1

        # defination
        n = len(nums)
        left = 0
        # 我们定义target在左闭右开的区间里，[left, right)
        right = n
        result = -1

        # terminator
        if n <= 0:
            return -1

        # process
        # [left,right)
        while left < right:
            mid = left + ((right - left) >> 1)
            if target < nums[mid]:
                # target 在左区间，因为是左闭右开的区间，nums[middle]一定不是我们的目标值，所以right = middle，在[left, middle)中继续寻找目标值
                right = mid
            elif target > nums[mid]:
                # target 在 [mid+1,right)之间
                left = mid + 1
            else:
                # 数组中找到目标值的情况
                result = mid
                break

        # return
        return result
