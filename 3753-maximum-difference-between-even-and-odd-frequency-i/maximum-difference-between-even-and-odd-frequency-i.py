class Solution:
    def maxDifference(self, s: str) -> int:
        odd=[]
        even=[]
        di={}
        for i in s:
            di[i]=di.get(i,0)+1
        for value in di.values():
            if value%2==0:
                even.append(value)
            if value%2==1:
                odd.append(value)
        return max(odd)-min(even)
        
        