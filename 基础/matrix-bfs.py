#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2020/12/14 21:38:08
@Author  :   sam.qi
@Version :   1.0
@Desc    :   矩阵(图)深度搜索
'''

import time
values = []


def dfs(nums, i, j):
    # terminator
    if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0]) or nums[i][j] == "0":
        return

    nums[i][j] = "0"
    dfs(nums, i+1, j)
    dfs(nums, i, j+1)
    dfs(nums, i-1, j)
    dfs(nums, i, j-1)


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "1"]
    ]
    dfs(grid, 0, 0)
