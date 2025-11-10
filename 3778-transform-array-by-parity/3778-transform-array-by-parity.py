class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                k.append(0)
            else:
                k.append(1)
        return sorted(k)
        