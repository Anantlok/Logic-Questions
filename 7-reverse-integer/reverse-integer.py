class Solution(object):
    def reverse(self, x):
        c=abs(x)
        b="".join(reversed(str(c)))
        if (int(b)<(2**31)-1):
            if x<0:
                return(-1*int(b))
            else:
                return(int(b))
        else:
            return 0
        