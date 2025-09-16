class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(0,len(nums)):
            if nums[i]==0:
                nums.append(0)
                nums.remove(nums[i])
        return nums
        