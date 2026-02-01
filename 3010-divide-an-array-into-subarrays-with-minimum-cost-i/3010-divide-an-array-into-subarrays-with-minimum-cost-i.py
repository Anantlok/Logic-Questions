class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        i=float('inf')
        j=float('inf')
        for x in nums[1:]:
            if x<i:
                j=i
                i=x
            elif x<j:
                j=x
        return nums[0]+i+j
        