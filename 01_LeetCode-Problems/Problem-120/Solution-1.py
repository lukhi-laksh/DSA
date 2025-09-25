"""
Triangle

"""
class Solution:
    def minimumTotal(self, triangle):
        for i in reversed(range(len(triangle) - 1)):
            for j in range(0, i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
    
    
sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))

"""
Time Complexity: O(n²)
Space Complexity: O(1)

"""