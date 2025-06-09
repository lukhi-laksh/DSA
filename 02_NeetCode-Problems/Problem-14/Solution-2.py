from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)
        size = len(height)
        f = [height[0]]
        for i in range(1, size):
            f.append(max(f[i - 1], height[i]))
        print(f)

        l = [0] * size
        l[-1] = height[-1]
        for i in range(size - 2, -1, -1):
            l[i] = max(l[i + 1], height[i])
        print(l)

        trapped_water = 0
        for i in range(size):
            trapped = min(f[i], l[i]) - height[i]
            print(trapped)
            trapped_water += trapped
        return trapped_water 


sol = Solution()
height = [4,2,0,3,2,5] 
print(sol.trap(height))