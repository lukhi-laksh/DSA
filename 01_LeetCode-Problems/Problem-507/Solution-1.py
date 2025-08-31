"""
Perfect Number

"""
class Solution(object):
    def checkPerfectNumber(self, num):
        
        laksh = num
        for i in range(1, (num//2)+1, 1):
            if num % i == 0:
                laksh = laksh - i
                
        return laksh == 0
        
        

sol = Solution()
print(sol.checkPerfectNumber(28))

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""