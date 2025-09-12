"""
House Robber

"""
class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

sol = Solution()
nums = [5, 2, 3, 20]
print(sol.rob(nums))

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""