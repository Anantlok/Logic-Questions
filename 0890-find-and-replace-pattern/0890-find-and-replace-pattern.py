class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def normalize(s):
            mp = {}
            arr = []
            next_id = 0
            for ch in s:
                if ch not in mp:
                    mp[ch] = next_id
                    next_id += 1
                arr.append(mp[ch])
            return arr
        
        p_norm = normalize(pattern)
        
        ans = []
        for w in words:
            if normalize(w) == p_norm:
                ans.append(w)
        return ans