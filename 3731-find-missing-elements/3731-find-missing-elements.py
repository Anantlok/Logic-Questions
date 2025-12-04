class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                k.append(i)
        return sorted(k)