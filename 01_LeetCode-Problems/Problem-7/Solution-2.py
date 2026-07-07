"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""
class Solution(object):
    def reverse(self, x):
        
        rev = 0
        mark = 0

        if x < 0:
            mark = 1
            x = abs(x)

        while x > 0:
            digit = x % 10
            rev = (rev * 10) + digit
            x = x // 10
    
        if mark == 1:
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else:
                return -rev
        else:
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else:
                return rev

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""