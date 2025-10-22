class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        maxx=window/k
        for i in range(k,len(nums)):
            window=window-nums[i-k]+nums[i]
            if window/k>maxx:
                maxx=window/k
        return maxx
        