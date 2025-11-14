"""
Increment Submatrics by One

"""

class Solution(object):
    def rangeAddQueries(self, n, queries):
        lineSweep = [[0]*(n+1) for i in range(n+1)]
        for q in queries:
            for r in range(q[0], q[2]+1):
                lineSweep[r][q[1]] += 1
                lineSweep[r][q[3]+1] -= 1
        grid = [[0]*n for _ in range(n)]
        for r in range(n):
            cur = 0
            for c in range(n):
                cur += lineSweep[r][c]
                grid[r][c] = cur
        return grid
    

"""
Time Complexity: O(n² + q × n)
Space Complexity: O(n²)

"""