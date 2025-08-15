class Solution(object):
    def countAndSay(self, n):
        k=1
        x="1"
        while k<n:
            y = ""
            i = 0
            while i<len(x):
                count=1
                while i+count<len(x) and x[i+count]==x[i]:
                    count=count+1
                y=y+str(count)+x[i]
                i=i+count
            x=y
            k=k+1
        return x


        