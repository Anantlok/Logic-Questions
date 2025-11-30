class Solution:
    def maxDistinct(self, s: str) -> int:
        k=[]
        count=0
        for i in s:
            if i not in k:
                k.append(i)
                count=count+1
        return count
        