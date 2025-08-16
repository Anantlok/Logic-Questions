class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                count=count+0
            if s[i]!=" ":
                count=count+1
            if s[i]==" " and count>0:
                break
        return (count)

       
        