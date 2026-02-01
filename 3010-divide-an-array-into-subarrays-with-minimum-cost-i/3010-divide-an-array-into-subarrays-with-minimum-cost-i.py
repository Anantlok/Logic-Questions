class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        k=nums[0]
        rest=sorted(nums[1:])
        print(k,rest[0],rest[1])
        return k+rest[0]+rest[1]
        