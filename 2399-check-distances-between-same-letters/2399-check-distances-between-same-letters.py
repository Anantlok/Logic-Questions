class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = {}
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')

            if ch not in first:
                first[ch] = i
            else:
                if i - first[ch] - 1 != distance[idx]:
                    return False
        
        return True