class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ans=ans+list(str(i))
        anss=[int(x) for x in ans]
        return anss