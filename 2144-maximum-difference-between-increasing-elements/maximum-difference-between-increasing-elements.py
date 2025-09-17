class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        d=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                k=nums[j]-nums[i]
                d.append(k)
        if max(d)<=0:
            return -1 
        return max(d)

        