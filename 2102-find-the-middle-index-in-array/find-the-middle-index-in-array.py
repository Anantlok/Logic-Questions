class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if (sum(nums[0:i]))==(sum(nums[i+1:len(nums)+1])):
                return i
        return -1
        