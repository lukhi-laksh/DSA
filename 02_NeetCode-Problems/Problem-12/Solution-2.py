from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return ([start + 1, end + 1])

            elif numbers[start] + numbers[end] > target:
                end = end - 1
            elif numbers[start] + numbers[end] < target:
                start = start + 1
        return []   


sol = Solution()
numbers = [1, 2, 3, 4]
target = 3
print(sol.twoSum(numbers, target))