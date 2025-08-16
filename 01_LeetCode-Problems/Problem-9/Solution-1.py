"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
        
        x_str = str(x)
        left = 0
        right = len(x_str) - 1      

        while left < right:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        return True

sol = Solution()
x = -1221
print(sol.isPalindrome(x))

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""