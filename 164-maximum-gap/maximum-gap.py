class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        snums=sorted(nums)
        k=[snums[i]-snums[i-1] for i in range(1,len(snums))]
        k.append(0)
        return max(k)
        