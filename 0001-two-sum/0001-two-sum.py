class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            k=i+1
            while k<len(nums):
                if nums[i]+nums[k]==target:
                    return [i,k]
                k+=1
        
                    


        