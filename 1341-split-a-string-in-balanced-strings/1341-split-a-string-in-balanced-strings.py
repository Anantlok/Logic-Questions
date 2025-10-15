class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        res = 0
        for ch in s:
            if ch == 'R':
                count += 1
            else: 
                count -= 1
            if count == 0:
                res += 1
        return res
        