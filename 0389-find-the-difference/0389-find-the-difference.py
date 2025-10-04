class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sk=sorted(list(s))
        tk=sorted(list(t))
        for i in range (0,len(sk)):
            if tk[i]!=sk[i]:
                return tk[i]
        return tk[len(tk)-1]