class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # 60 is safe because 2^60 > 1e18
            x = num1 - num2 * k
            if x < 0:
                continue
            ones = bin(x).count('1')
            if ones <= k <= x:
                return k
        return -1
        