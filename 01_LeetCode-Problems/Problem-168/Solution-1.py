"""
Excel Sheet Column Title

"""
class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ''
        
        while columnNumber > 0:
            columnNumber -= 1
            res = chr((columnNumber % 26) + ord('A')) + res
            columnNumber //= 26
            
        return res

sol = Solution()
print(sol.convertToTitle(22569))

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""