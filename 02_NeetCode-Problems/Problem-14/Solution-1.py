from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)
        size = len(height)
        f = list()
        f = [height[0]]
        for i in range(1, size):
            if height[i] > f[i - 1]:
                f.append(height[i])
            else:
                f.append(f[i - 1])
        print(f)

        l = [0] * (size)
        l[-1] = height[-1]
        for i in range(size - 2, -1, -1):
            if height[i] > l[i + 1]:
                l[i] = height[i]
            else:
                l[i] = l[i + 1]
        print(l)

        empty = [0] * size 
        for i in range(size):
            if f[i] < l[i]:
                min_hight = f[i]
            else:
                min_hight = l[i]
            empty[i] = max(0, min_hight - height[i])
        return sum(empty)

sol = Solution()
height = [4,2,0,3,2,5] 
print(sol.trap(height))