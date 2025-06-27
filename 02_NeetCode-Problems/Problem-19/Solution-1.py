from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return ans
                    
                    
sol = Solution()
temperatures = [30, 38, 30, 36, 35, 40, 28]
print(sol.dailyTemperatures(temperatures))