class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
    
        for i in range(0, len(s), k):
            substring = s[i:i+k]
            total = 0
            
            for ch in substring:
                total += ord(ch) - ord('a')
            
            hashed_char = chr((total % 26) + ord('a'))
            result.append(hashed_char)
        
        return "".join(result)
        