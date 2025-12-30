"""
Magic Square in Grid

"""


class Solution(object):
    def numMagicSquaresInside(self, grid):

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        def isMagicSquare(x, y):
            s = set()
            for i in range(3):
                for j in range(3):
                    if grid[x + i][y + j] < 1 or grid[x + i][y + j] > 9:
                        return False
                    s.add(grid[x + i][y + j])
            
            if len(s) != 9:
                return False
            
            rows = [sum(grid[x + i][y:y + 3]) for i in range(3)]
            cols = [sum(grid[x + i][y + j] for i in range(3)) for j in range(3)]
            diag1 = sum(grid[x + i][y + i] for i in range(3))
            diag2 = sum(grid[x + i][y + 2 - i] for i in range(3))
            
            return (rows[0] == rows[1] == rows[2] == cols[0] == cols[1] == cols[2] == diag1 == diag2)

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagicSquare(i, j):
                    count += 1
        
        return count

"""
Time Complexity: O(n · m)
Space Complexity: O(1)

"""