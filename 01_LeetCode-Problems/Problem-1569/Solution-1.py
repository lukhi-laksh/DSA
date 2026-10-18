"""
Number of Ways to Reorder Array to Get Same BST

"""
MOD = 10**9 + 7

class Solution(object):
    def numOfWays(self, nums):

        def count_ways(nums):
            if len(nums) <= 2:
                return 1

            root = nums[0]
            left_nums = [num for num in nums[1:] if num < root]
            right_nums = [num for num in nums[1:] if num > root]

            left_ways = count_ways(left_nums)
            right_ways = count_ways(right_nums)

            num_ways = (
                self.combination(len(nums) - 1, len(left_nums)) * 
                left_ways * right_ways
            )

            return num_ways

        return (count_ways(nums) - 1) % MOD

    def combination(self, n, k):
        if k > n - k:
            k = n - k

        res = 1
        for i in range(k):
            res = (res * (n - i)) // (i + 1)

        return res
    
"""
Time Complexity: O(n * h)
Space Complexity: O(n * h)

"""