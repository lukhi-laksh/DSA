from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
lists = [2, 3, 4, 5, 6, 20, 11]
print(sol.longestConsecutive(lists))