class Solution(object):
    def myPow(self, x, n):        
        def Custom(x, n):
            
            if (n == 0):
                return 1
            if n < 0:
                return 1 / Custom(x, -n)
            if n % 2 == 0:
                return Custom(x * x, n // 2)
            else:
                return x * Custom(x, n - 1)
        return Custom(x, n)
        

sol = Solution()

print(sol.myPow(2.0000, -2))