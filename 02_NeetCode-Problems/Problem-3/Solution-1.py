from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        index = list()
        for i in range(l):
            for j in range(i+1, l):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return []
            

sol = Solution()

lists = [1, 3, 4, 6, 3, 5]
target = 4
print(sol.twoSum(lists, target))