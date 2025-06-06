from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []


sol = Solution()
numbers = [2, 3, 5, 6, 7]
target = 10
print(sol.twoSum(numbers, target))