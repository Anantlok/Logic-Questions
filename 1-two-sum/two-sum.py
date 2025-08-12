class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    ans=[0,0]
                    ans[0]=i
                    ans[1]=j
                    return ans  