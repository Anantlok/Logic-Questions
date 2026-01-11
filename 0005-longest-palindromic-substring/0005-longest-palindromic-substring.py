class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=0
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1
        for i in range(0,len(s)):
            len1=expand(i,i)
            len2=expand(i,i+1)
            maxlen=max(len1,len2)
            if maxlen>end-start:
                start=i-(maxlen-1)//2
                end=i+maxlen//2
        return s[start:end+1]