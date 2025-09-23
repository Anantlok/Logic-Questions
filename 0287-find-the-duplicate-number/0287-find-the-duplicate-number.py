class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            di[i]=di.get(i,0)+1
        for key,values in di.items():
            if values>1:
                return key