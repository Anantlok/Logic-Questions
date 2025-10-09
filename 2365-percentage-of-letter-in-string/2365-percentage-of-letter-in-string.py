class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0
        for i in s:
            if i==letter:
                count=count+1
        per=(count/len(s))*100
        return int(per)
            