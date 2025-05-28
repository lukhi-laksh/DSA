from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            temp = target - i 
            if temp in nums:
                for j in range(len(nums)):
                    if nums[j] == temp:
                        return [nums.index(i), j]

Sol = Solution()
lists = [1, 2, 5, 6, 9]
target = 15    
print(Sol.twoSum(lists, target))
