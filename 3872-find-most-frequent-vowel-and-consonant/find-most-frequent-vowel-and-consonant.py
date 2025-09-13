class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"
        cons={"":0}
        vows={"":0}
        for i in s:
            if i in vowels:
                vows[i]=vows.get(i,0)+1
            if i not in vowels:
                cons[i]=cons.get(i,0)+1
        maxC=max(cons.values())
        maxV=max(vows.values())
        return maxC+maxV
        