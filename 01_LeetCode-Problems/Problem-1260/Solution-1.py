"""
Shift 2D grid

"""

class Solution(object):
    def shiftGrid(self, grid, k):

        m,n = len(grid), len(grid[0])
        total = m*n
        k = k%total

        ans = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                oldIndex = (row*n) + col
                newIndex = (oldIndex + k ) % total

                newRow = newIndex // n
                newCol = newIndex % n

                ans[newRow][newCol] = grid[row][col]
        
        return ans

"""
Time Complexity:  O(2ⁿ)
Space Complexity: O(n)

"""