class Solution(object):
    def isPowerOfFour(self, n):
        for i in range(31):
            if n==4**i:
                return True
        return False
        