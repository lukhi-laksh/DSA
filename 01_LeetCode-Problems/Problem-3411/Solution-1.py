"""
Maximum Subarray With Equal Products

"""
class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a // gcd(a, b)) * b

        n = len(nums)
        max_len = 0
        for i in range(n):
            current_prod = 1
            current_gcd = nums[i]
            current_lcm = nums[i]
            for j in range(i, n):
                if current_prod > 1000000000000 // nums[j]:
                    current_prod = 2000000000000
                else:
                    current_prod *= nums[j]

                if j > i:
                    current_gcd = gcd(current_gcd, nums[j])
                    current_lcm = lcm(current_lcm, nums[j])

                if current_prod == current_lcm * current_gcd:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
        return max_len

"""
Time Complexity: O(n² log m)
Spce Complexity: O(1)

"""