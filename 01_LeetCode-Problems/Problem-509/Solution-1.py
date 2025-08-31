"""
Fibonacci Number

"""
class Solution(object):
    def fib(self, n):
        def custom(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            return custom(n-1) + custom(n-2)
        
        return custom(n)
    
    

sol = Solution()
print(sol.fib(30))

"""
Time Complexity:  O(2ⁿ)
Space Complexity: O(n)

"""