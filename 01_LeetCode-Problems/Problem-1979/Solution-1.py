"""
Find Greatest Common Divisor of Array

"""

class Solution(object):
    def findGCD(self, nums):
        nums.sort()

        small = nums[0]
        large = nums[-1]
        ans = 1

        for i in range(1, small + 1):
            if small % i == 0 and large % i == 0:
                ans = i

        return ans

"""
Time Complexity:  O()
Space Complexity: O(n)

"""