"""
Roman to Integer

"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        num = 0
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for c in s:
            if roman[c] > num:  
                total += roman[c] - 2 * num
            else:
                total += roman[c]
            num = roman[c]

        return total
    
sol = Solution()
print(sol.romanToInt("MCMXCIV"))

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""