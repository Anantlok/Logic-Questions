class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        d=nums[-k:]+nums[:-k]
        for i in range(0,len(nums)):
            nums[i]=d[i]
        return nums