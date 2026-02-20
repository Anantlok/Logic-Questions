class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0,float('-inf'),float('-inf')]
        for i in nums:
            temp=dp[:]
            for prev in temp:
                if prev != float('-inf'):
                    new_sum=prev+i
                    remainder=new_sum%3
                    dp[remainder]=max(dp[remainder],new_sum)
        return dp[0]


        