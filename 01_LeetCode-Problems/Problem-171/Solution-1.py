"""
Excel Sheet Column Number

"""

class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char.upper()) - ord('A') + 1)
        return result

sol = Solution()
print(sol.titleToNumber("AB"))

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""

