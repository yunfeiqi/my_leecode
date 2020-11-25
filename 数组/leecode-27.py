
'''
直接遍历数据
'''


# 覆盖法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # defination
        idx = 0
        for num in nums:
            # 不相等，则赋值到原来相等的地方
            if val != num:
                nums[idx] = num
                idx += 1

        return idx


'''
将相同的元素全部移动到右面
'''

# 双指针交换法[head, tail]


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # defination

        # unequals index
        head = 0
        # equals index
        tail = len(nums)

        # process
        while head < tail:
            if nums[head] == val:
                # exchange the head and tial
                nums[head] = nums[tail-1]
                # tail to left one step
                tail = tail - 1
            else:
                # head to right one step
                head = head + 1

        # return
        return head
