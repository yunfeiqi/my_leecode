
# 二分法查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = len(nums)
        left = 0
        right = idx - 1

        # [left,right] 闭区间
        while left <= right:
            idx = left + (right - left) // 2
            if target < nums[idx]:
                right = idx - 1
            elif target > nums[idx]:
                left = idx + 1
            else:
                break

        return idx
