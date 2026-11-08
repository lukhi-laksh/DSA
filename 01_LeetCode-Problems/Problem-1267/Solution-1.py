"""
Count Servers That can Communicate

"""

class Solution(object):
    def countServers(self, grid):
        m,n = len(grid),len(grid[0])
        columns=[0]*n
        rows = [0]*m
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    columns[j]+=1
                    rows[i]+=1
        

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (columns[j]>1 or rows[i]>1):
                    count+=1
        return count

