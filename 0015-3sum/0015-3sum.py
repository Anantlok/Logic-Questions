class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[i]<0:
                    left+=1
                elif nums[left]+nums[right]+nums[i]>0:
                    right-=1
                else:
                    res.append([nums[left],nums[right],nums[i]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left=left+1
                    right=right-1
        return res