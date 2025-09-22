class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        if len(nums)==0:
            return 0
        for i in nums:
            d[i]=d.get(i,0)+1
        kmax=max(d.values())
        b=0
        for j in d.values():
            if j==kmax:
                b=b+j
        return b
