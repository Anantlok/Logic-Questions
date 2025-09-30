class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        k=[]
        for i in range(len(nums)-1):
            sums=(nums[i]+nums[i+1])%10
            k.append(sums)
        return self.triangularSum(k)
        