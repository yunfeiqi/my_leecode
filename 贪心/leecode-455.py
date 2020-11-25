'''
https://mp.weixin.qq.com/s/YSuLIAYyRGlyxbp9BNC1uw
'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # defination
        s_size = len(s)
        g_size = len(g)
        num = 0

        # terminator
        if s_size <= 0:
            return 0

        # process

        # sort
        g.sort()
        s.sort()

        # foreach
        s_index = s_size - 1
        for g_index in range(g_size-1, -1, -1):
            if s_index >= 0 and g[g_index] <= s[s_index]:
                num += 1
                s_index -= 1

        # return
        return num
