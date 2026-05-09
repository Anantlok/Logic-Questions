class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            vals = []

            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            # top row
            for j in range(left, right + 1):
                vals.append(grid[top][j])

            # right column
            for i in range(top + 1, bottom):
                vals.append(grid[i][right])

            # bottom row
            for j in range(right, left - 1, -1):
                vals.append(grid[bottom][j])

            # left column
            for i in range(bottom - 1, top, -1):
                vals.append(grid[i][left])

            # rotate counter-clockwise by k
            r = k % len(vals)
            vals = vals[r:] + vals[:r]

            idx = 0

            # fill top row
            for j in range(left, right + 1):
                grid[top][j] = vals[idx]
                idx += 1

            # fill right column
            for i in range(top + 1, bottom):
                grid[i][right] = vals[idx]
                idx += 1

            # fill bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = vals[idx]
                idx += 1

            # fill left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = vals[idx]
                idx += 1

        return grid