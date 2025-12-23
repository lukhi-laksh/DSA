"""
Factorial Trailing Zeros

"""

class Solution(object):
    def trailingZeroes(self, n):

        def factorial(n):
            factorial = 1
            while n != 0:
                factorial *= n
                n -= 1
            return factorial
        
        fact = str(factorial(n))
        ans = 0
        for i in range(len(fact)-1, -1, -1):
            if fact[i] != '0':
                break
            ans += 1
        return ans
    
"""
Time Complexity: O(n)
Space Complexity: O(n)

"""

        