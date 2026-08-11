"""
Smallet Missing Interger Greter then Sequential Prefix Sum

"""
class Solution:
    def missingInteger(self, nums):
        
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        st = set(nums)

        while total in st:
            total += 1

        return total

"""

Time Complexity:  O(n)
Space Complexity: O(n)

"""