class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        k=0
        while 3**k<=n:
            if 3**k==n:
                return True
            k=k+1
        return False
