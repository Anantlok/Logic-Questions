class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)
        
        # Sort times
        minutes.sort()
        
        # Initialize result
        min_diff = float('inf')
        
        
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        
        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])
        
        return min_diff
        