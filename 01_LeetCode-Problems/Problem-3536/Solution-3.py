"""
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

"""
import math
class Solution(object):
    def maxProduct(self, n):
        array = [int(digit) for digit in str(n)]
        
        if len(array) == 0:
            return 0
        elif len(array) == 1:
            return array[0]
        elif len(array) <=2:
            return array[0] * array[1]

        array.sort()
        
        return array[-1] * array[-2]
        
sol = Solution()
n = 5
print(sol.maxProduct(n))


"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""