class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        output=0
        for i in range(0,len(nums)):
            if i%2==0:
                output=output+nums[i]
            else:
                output=output-nums[i]

        return output