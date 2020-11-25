
# 模拟生成
class Solution:
    def generateMatrix(self, n: int):
        # defination

        left = 0
        right = n-1

        top = 0
        bottom = n-1

        nums = n ** 2
        mat = [[0 for _ in range(n)] for _ in range(n)]

        # terminator
        if n == 1:
            return [[1]]

        # process
        num = 1
        while num <= nums:
            # left to right on top edge
            for i in range(left, right+1):
                mat[top][i] = num
                num += 1
            top += 1

            # top to bottom on right edge
            for i in range(top, bottom + 1):
                mat[i][right] = num
                num += 1
            right -= 1

            # right to left on bottom edge
            for i in range(right, left-1, -1):
                mat[bottom][i] = num
                num += 1
            bottom -= 1

            # bottom to top on left edge
            for i in range(bottom, top-1, -1):
                mat[i][left] = num
                num += 1
            left += 1
        # return
        return mat
