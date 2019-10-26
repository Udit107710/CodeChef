# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_left_right = [max(x) for x in grid]
        top_bottom = []
        for i in range(0, len(grid)):
            top_bottom.append([x[i] for x in grid])
        max_top_bottom = [max(x) for x in top_bottom]
        
        height = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                height += min(max_top_bottom[i], max_left_right[j]) - grid[i][j]
        return height