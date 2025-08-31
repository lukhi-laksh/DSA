"""
Plus one

"""

class Solution(object):
    def plusOne(self, digits):
        length = len(digits) - 1
        
        if (digits[length] == 9):
            temp = length
            while digits[temp] == 9:
                digits[temp] = 0
                temp -= 1
            digits[temp] += 1

        else:
            digits[length] += 1
        return digits

sol = Solution()
digits = [2, 9, 9]
print(sol.plusOne(digits))