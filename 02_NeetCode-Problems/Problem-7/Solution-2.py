from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in new_nums:
                length = 0
                while (num + length) in new_nums:
                    length += 1
                longest = max(length, longest)
        return longest

                

sol = Solution()
nums = [2, 3, 4, 5, 2, 6, 7, 30, 11]
print(sol.longestConsecutive(nums))