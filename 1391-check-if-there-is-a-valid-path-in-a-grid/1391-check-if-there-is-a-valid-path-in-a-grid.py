class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # directions for each type
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = [[False]*n for _ in range(m)]
        
        # use list as queue
        q = [(0, 0)]
        visited[0][0] = True
        
        while q:
            x, y = q.pop(0)   # remove front
            
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    
                    # check reverse connection
                    for bdx, bdy in dirs[grid[nx][ny]]:
                        if nx + bdx == x and ny + bdy == y:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            break
        
        return False
        