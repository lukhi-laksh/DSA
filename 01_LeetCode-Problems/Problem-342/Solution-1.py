"""
Power of Four

"""
class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1
    
sol = Solution()
print(sol.isPowerOfFour(15))

"""
Time Complexity:  O(log n)
Space Complexity: O(1)

"""