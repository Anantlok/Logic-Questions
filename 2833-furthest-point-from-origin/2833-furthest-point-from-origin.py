class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count('L')
        right = moves.count('R')
        blank = moves.count('_')
        
        pos = right - left
        
        return abs(pos) + blank
        