"""
Sum of Sortable Integers

"""

class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            rotated = []
            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                m = len(block)
                drops = [i for i in range(m - 1) if block[i] > block[i + 1]]

                if len(drops) > 1:
                    valid = False
                    break

                if len(drops) == 1:
                    p = drops[0] + 1
                    block = block[p:] + block[:p]

                if block != sorted(block):
                    valid = False
                    break

                rotated.extend(block)

            if valid and rotated == sorted(nums):
                ans += k

        return ans

"""
Time Complexity: O(n² log n)
Space Complexity: O(n)

"""