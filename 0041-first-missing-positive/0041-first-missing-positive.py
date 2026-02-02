class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i < n:
            if 1 <= nums[i] <= n:
                correct = nums[i] - 1
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                    continue
            i += 1   
        for i in range(0,len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
        