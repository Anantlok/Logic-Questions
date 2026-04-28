class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            for val in row:
                arr.append(val)
        remainder = arr[0] % x
        for val in arr:
            if val % x != remainder:
                return -1
        
        arr.sort()
        
        n = len(arr)
        median = arr[n // 2]
        
        operations = 0
        for val in arr:
            operations += abs(val - median) // x
        
        return operations
        