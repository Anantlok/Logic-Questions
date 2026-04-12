class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_pos(c):
            idx = ord(c) - ord('A')
            return (idx // 6, idx % 6)
        
        # Distance function
        def dist(a, b):
            if a is None:
                return 0
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        n = len(word)
        
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == n:
                return 0
            
            curr = get_pos(word[i])
            
            # Move finger 1
            cost1 = dist(f1, curr) + dp(i + 1, curr, f2)
            
            # Move finger 2
            cost2 = dist(f2, curr) + dp(i + 1, f1, curr)
            
            return min(cost1, cost2)
        
        return dp(0, None, None)
        