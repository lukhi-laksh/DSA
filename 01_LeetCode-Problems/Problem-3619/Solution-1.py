class Solution(object):
    def countIslands(self, grid, k):

        n=len(grid)
        m=len(grid[0])
        count=0
        x=0
        def dfs(i,j):
            
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0 :
                return 0
            x=grid[i][j]
            grid[i][j]=0

            x+=dfs(i-1,j)
            x+=dfs(i,j-1)
            x+=dfs(i+1,j)
            x+=dfs(i,j+1)

            return x

    
        for i in range(n):
            for j in range(m):
                x=0
                if grid[i][j]!=0:
                    y=dfs(i,j)
                    if y%k==0:
                        count+=1

        return count
        
            