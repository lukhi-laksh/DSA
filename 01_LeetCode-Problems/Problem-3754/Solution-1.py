"""
Concatenate Non-Zero Digits and Multiply by Sum I

"""
class Solution(object):
    def sumAndMultiply(self, n):
        sum = 0
        need = 0

        for i in str(n):
            if i == '0':
                pass
            else:
                need = (need * 10) + int(i)
                sum += int(i)

        return sum * need

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""