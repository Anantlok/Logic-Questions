class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minn=abs(nums[0])
        for i in nums:
            minn=min(minn,abs(i))
        if minn in nums:
            return minn
        else: return -1*minn