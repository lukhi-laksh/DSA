class Solution:
    def smallestNumber(self, n):
        bit = n.bit_length()
        ans = (1 << bit) - 1
        return ans

sol = Solution()
print(sol.smallestNumber(5))