"""
Roman to Integer

"""

class Solution(object):
    def romanToInt(self, s):
        dictt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = 0
        for i in range(len(s) - 1):
            if dictt[s[i]] < dictt[s[i + 1]]:
                n -= dictt[s[i]]
            else:
                n += dictt[s[i]]
            
        return n + dictt[s[-1]]

sol = Solution()
print(sol.romanToInt("MCMXCIV"))

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""