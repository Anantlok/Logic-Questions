class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nk= len(nums)
    
        for i in range(nk):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
    
        for i in range(nk):
            if nums[i] != i + 1:
                return i + 1

        return nk + 1