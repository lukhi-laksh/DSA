class Solution(object):
    def countNegatives(self, grid):

        counter = 0

        row = len(grid) - 1
        col = 0

        while row >=0 and col < len(grid[0]):
            
            if grid[row][col] < 0:
                counter += len(grid[0]) - col
                row -= 1

            else:
                col +=1

        return counter
                