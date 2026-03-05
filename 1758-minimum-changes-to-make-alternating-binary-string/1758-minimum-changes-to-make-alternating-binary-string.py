class Solution:
    def minOperations(self, s: str) -> int:
        change_start_with_0 = 0
        change_start_with_1 = 0
        
        for i in range(len(s)):
            
            expected0 = '0' if i % 2 == 0 else '1'
            
            
            expected1 = '1' if i % 2 == 0 else '0'
            
            if s[i] != expected0:
                change_start_with_0 += 1
            
            if s[i] != expected1:
                change_start_with_1 += 1
        
        return min(change_start_with_0, change_start_with_1)