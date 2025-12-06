class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                a = words[i]
                b = words[j]
                
                if b.startswith(a) and b.endswith(a):
                    count += 1
                    
        return count