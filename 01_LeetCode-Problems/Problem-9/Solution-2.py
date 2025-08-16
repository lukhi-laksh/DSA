"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = list(str(x))
            
        z = y[::-1]
        return y==z

sol = Solution()
x = -1221
print(sol.isPalindrome(x))

