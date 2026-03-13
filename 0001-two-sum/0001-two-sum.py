class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,j in enumerate(nums):
            remainder=target-j
            if remainder in dic:
                return [dic[remainder],i]
            dic[j]=i

        