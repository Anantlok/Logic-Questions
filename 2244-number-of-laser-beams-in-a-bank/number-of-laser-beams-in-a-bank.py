class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        device_counts = [row.count('1') for row in bank if '1' in row]
    
        total_beams = 0
        for i in range(1, len(device_counts)):
            total_beams += device_counts[i - 1] * device_counts[i]
    
        return total_beams