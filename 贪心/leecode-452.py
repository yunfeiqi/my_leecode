class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # defination
        size = len(points)

        # terminator
        if size <= 0:
            return 0

        # process

        # sort
        points.sort()

        # greed shoot
        num = 1
        p_left = points[0][0]
        p_right = points[0][1]

        for idx in range(1, size):
            if points[idx][0] <= p_right:
                # update common overlap area
                p_left = points[idx][0]
                if points[idx][1] < p_right:
                    p_right = points[idx][1]
            else:
                num += 1
                p_left = points[idx][0]
                p_right = points[idx][1]

        # return
        return num
