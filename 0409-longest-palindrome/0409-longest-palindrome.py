class Solution:
    def longestPalindrome(self, s: str) -> int:
        di={}
        for i in s:
            di[i]=di.get(i,0)+1
        count=0
        odd_found=False
        for i in di.values():
            count += (i // 2) * 2   
            if i % 2 == 1:          
                odd_found = True
        if odd_found:
            count=count+1
        return count
        