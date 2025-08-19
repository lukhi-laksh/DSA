"""
Integer to Roman
"""
class Solution(object):
    def intToRoman(self, num):
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        ans = ""
        for key, symbol in values:
            while num >= key:
                ans += symbol
                num -= key
        return ans


# test
sol = Solution()
print(sol.intToRoman(3566))   # MMMDLXVI


"""
Time Complexity:  O(d) = log(n)
Space Complexity: O(d) = log(n)

"""
