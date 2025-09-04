class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xk=abs(z-x)
        yk=abs(z-y)
        if xk<yk:
            return 1
        if yk<xk:
            return 2
        else:
            return 0
        