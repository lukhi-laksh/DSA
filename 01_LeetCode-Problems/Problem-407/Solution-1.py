"""
Trapping Rain Water 2

"""
class Solution(object):
    def trapRainWater(self, heightMap):

        m = len(heightMap)
        n = len(heightMap[0])
        trapped = 0
        visited = [[False for j in range(n)] for i in range(m)]

        import heapq
        myheap = []
        for i in range(m):
            heapq.heappush(myheap, (heightMap[i][0], i, 0))
            heapq.heappush(myheap, (heightMap[i][n-1], i, n-1))
            visited[i][0]=True
            visited[i][n-1]= True

        for j in range(1, n-1):
            heapq.heappush(myheap, (heightMap[0][j], 0, j))
            heapq.heappush(myheap, (heightMap[m-1][j], m-1, j))
            visited[0][j]=True
            visited[m-1][j]= True
        
        level = 0
        while myheap:
            t = heapq.heappop(myheap)
            level = max(level, t[0])
            trapped+= level - t[0]

            if t[1]>0 and not visited[t[1]-1][t[2]]:
                heapq.heappush(myheap, (heightMap[t[1]-1][t[2]], t[1]-1, t[2]))
                visited[t[1]-1][t[2]] = True
            if t[1]<m-1 and not visited[t[1]+1][t[2]]:
                heapq.heappush(myheap, (heightMap[t[1]+1][t[2]], t[1]+1, t[2]))
                visited[t[1]+1][t[2]] = True
            if t[2]<n-1 and not visited[t[1]][t[2]+1]:
                heapq.heappush(myheap, (heightMap[t[1]][t[2]+1], t[1], t[2]+1))
                visited[t[1]][t[2]+1] = True
            if t[2]>0 and not visited[t[1]][t[2]-1]:
                heapq.heappush(myheap, (heightMap[t[1]][t[2]-1], t[1], t[2]-1))
                visited[t[1]][t[2]-1] = True
        return trapped
    
    
sol = Solution()
print(sol.trapRainWater([3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3]))