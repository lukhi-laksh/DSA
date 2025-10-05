"""
Pacific Atlantic Water Flow

"""

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # # check side case
        # if not heights:
        #     return
        
        
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # like a worker hahaha
        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # traverse nbrs
            for d in dirs:
                next_i, next_j = i + d[0], j + d[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # question-specific checks:
                    if heights[next_i][next_j] >= heights[i][j]:
                        traverse(next_i, next_j, visited)
        
        pacific, atlantic = set(), set()
        for i in range(rows):
            traverse(i, 0, pacific)
            traverse(i, cols - 1, atlantic)
        for j in range(cols):
            traverse(0, j, pacific)
            traverse(rows - 1, j, atlantic)
            
        return [list(item) for item in pacific & atlantic]

sol = Solution()
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

"""

Time Complexity: O(n)
Space Complexity: O(n)

"""