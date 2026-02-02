class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if 0<=nums[i]<len(nums):
                current=nums[i]
                if nums[current]!=nums[i]:
                    nums[i],nums[current]=nums[current],nums[i]
                    continue
            i+=1
        for i in range(0,len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)