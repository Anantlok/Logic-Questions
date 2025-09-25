class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = {}
    
        for word in (s1.split() + s2.split()):
            freq[word] = freq.get(word, 0) + 1
    
        result = []
        for word, count in freq.items():
            if count == 1:
                result.append(word)
    
        return result
        