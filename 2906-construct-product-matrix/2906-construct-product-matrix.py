class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        
        n, m = len(grid), len(grid[0])
        
        # Step 1: flatten
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % MOD)
        
        size = len(arr)
        
        # Step 2: prefix
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        # Step 3: suffix
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        # Step 4: result
        res = [0] * size
        for i in range(size):
            res[i] = (prefix[i] * suffix[i]) % MOD
        
        # Step 5: reshape back
        ans = [[0]*m for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(m):
                ans[i][j] = res[idx]
                idx += 1
        
        return ans
        