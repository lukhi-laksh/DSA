"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            temp = target - i 
            if temp in nums:
                for j in range(len(nums)):
                    if j[i] == temp:
                        return [i]
        return []
        
sol = Solution()
lists = [1,2,5,6,9]
target = 15
print(sol.twoSum(lists, target))

"""
Time Complexity: O(n²)
Space Complexity: O(1)

"""