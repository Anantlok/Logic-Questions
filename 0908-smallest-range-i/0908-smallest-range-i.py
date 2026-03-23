class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxx=max(nums)
        minn=min(nums)
        diff=maxx-minn
        ext=2*k
        if diff<=ext:
            return 0
        else: return diff-ext