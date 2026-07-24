"""
Shuffle the Array

"""

class Solution(object):
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])

        return ans

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""