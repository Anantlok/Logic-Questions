class Solution(object):
    def mySqrt(self, x):
        i=0
        while i*i<=x:
            if i*i==x:
                return i
            i=i+1
        return i-1
            
        