class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxx=0
        res=[]
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            if nums[i]==0:
                count=0
            res.append(count)
        return max(res)
            