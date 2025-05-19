"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

"""

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                temp = num
                current_strick = 1

                while temp + 1 in num_set:
                    temp += 1
                    current_strick += 1

                longest = max(longest, current_strick)

        return longest

sol = Solution()
nums = [1, 2, 3, 4, 2, 2, 4, 8]
print(sol.longestConsecutive(nums))

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""