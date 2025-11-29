"""
Minimum Operations to Make Array Sum Divisble by K

"""

class Solution(object):
    def minOperations(self, nums, k):
        i = 0
        while True:
            if (sum(nums)-i)% k == 0:
                return i
            else:
                i += 1

        return i 

sol = Solution()
print(sol.minOperations([3, 7, 9], 5))

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""