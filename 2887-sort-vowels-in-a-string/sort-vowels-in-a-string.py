class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s=list(s)
        vwlist=[ch for ch in s if ch in vowels]
        vwlist.sort()
        index=0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i]=vwlist[index]
                index+=1
        return "".join(s)
        