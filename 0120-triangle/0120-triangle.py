class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]   
        for row in reversed(triangle[:-1]):
            dp = [row[i] + min(dp[i], dp[i+1]) for i in range(len(row))]
        return dp[0]
        