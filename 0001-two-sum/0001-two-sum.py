class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,val in enumerate(nums):
            remainder=target-val
            if remainder in dic:
                return [dic[remainder],i]
            dic[val]=i
        
                    


        