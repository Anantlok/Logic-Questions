class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums=set(nums)
        maxx=0
        for i in nums:
            if i-1 not in nums:
                count=1
                current=i
                while current+1 in nums:
                    current=current+1
                    count=count+1
                maxx=max(maxx,count)
        return maxx
        