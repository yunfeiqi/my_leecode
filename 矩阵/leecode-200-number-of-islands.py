#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2020/12/08 16:07:37
@Author  :   sam.qi
@Version :   1.0
@Desc    :   网格中联通区域个数
'''


def dfs(nums, i, j):
    '''
        深度优先搜索，如果当前节点为 1 ，则重置为0 
    '''

    if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0]) or nums[i][j] == '0':
        return

    nums[i][j] = '0'
    dfs(nums, i+1, j)
    dfs(nums, i, j+1)
    dfs(nums, i-1, j)
    dfs(nums, i, j-1)


class Solution(object):
    def numIslands(self, nums):

        # terminator
        if nums is None or len(nums) <= 0:
            return 0

        values = 0

        num_rows = len(nums)
        cols_rows = len(nums[0])

        for row_id in range(num_rows):
            for col_id in range(cols_rows):
                if nums[row_id][col_id] == '1':
                    values += 1
                    dfs(nums, row_id, col_id)
        return values


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "1"]
    ]
    s = Solution()
    print(s.numIslands(grid))
