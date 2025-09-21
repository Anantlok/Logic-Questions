class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0,len(s)):
            d=s[i]
            s.replace(s[i]," ",1)
            if d not in s[i+1:len(s)] and d not in s[0:i]: 
                return i      
        return -1