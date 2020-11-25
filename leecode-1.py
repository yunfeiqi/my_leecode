

'''
@Desc    :   推荐
@Time    :   2020/09/29 12:14:58
@Author  :   sam.qi 
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []
        num_dict = {}

        # 简历倒排索引
        for idx, num in enumerate(nums):
            num_dict[num] = idx

        # 遍历和查询
        for obj_idx, num in enumerate(nums):
            sub_num = target - num
            sub_val = num_dict.get(sub_num, None)
            # 判断和条件界定
            if sub_val is not None and sub_val != obj_idx:
                result.append(obj_idx)
                result.append(num_dict[sub_num])
                break
        return result


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []
        num_dict = {}

        for idx, num in enumerate(nums):
            sub_value = target - num
            if num_dict.get(sub_value, None) is not None:
                result.append(idx)
                result.append(num_dict.get(sub_value))
                break
            else:
                num_dict[num] = idx
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
