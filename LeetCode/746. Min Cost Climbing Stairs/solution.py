"""
Problem:
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        
        dp = [None] * length
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        def calculate(dp, i):
            if i >= length:
                return 0
            elif dp[i] is not None:
                return dp[i]
            else:
                dp[i] = cost[i] + min(calculate(dp, i-1), calculate(dp, i-2))
                return dp[i]
            
        last = calculate(dp, length-1)
        
        return min(dp[length-2], last)