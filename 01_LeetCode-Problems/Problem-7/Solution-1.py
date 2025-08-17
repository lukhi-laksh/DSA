"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""
class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        ans = 0
        while x != 0:
            temp = x % 10
            x = x // 10
            ans = (ans * 10) + temp
        
