#idk
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            k = -int(str(x)[1:][::-1])
        else:
            k = int(str(x)[::-1])
        
        if k < -2**31 or k > 2**31 - 1:
            return 0
        
        return k
        
        