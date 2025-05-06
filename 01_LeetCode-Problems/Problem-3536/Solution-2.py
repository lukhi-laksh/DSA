"""
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

"""
import math
class Solution(object):
    def maxProduct(self, n):
        
        str_n = str(n)
        
        sorted_digits = sorted(str_n)
        
        return int(sorted_digits[-1]) * int(sorted_digits[-2])
        
sol = Solution()
n = 34
print(sol.maxProduct(n))


"""
Time Complexity:  O(d log d)
Space Complexity: O(d)

"""