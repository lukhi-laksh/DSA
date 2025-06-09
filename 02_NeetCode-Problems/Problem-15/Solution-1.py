from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        empty = list()
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                empty.append((j - i) * min(heights[i], heights[j]))
        return max(empty)
        


sol = Solution()
height = [1,7,2,5,4,7,3,6]
print(sol.maxArea(height))
height = [2, 2, 2]
print(sol.maxArea(height))
