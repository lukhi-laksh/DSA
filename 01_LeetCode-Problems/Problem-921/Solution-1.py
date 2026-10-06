"""
Minimum Add to Make Parentheses Valid

"""
class Solution:
    def minAddToMakeValid(self, s):
        o = 0
        e = 0

        for ch in s:
            if ch == '(':
                o += 1
            else:
                if o > 0:
                    o -= 1
                else:
                    e += 1

        return o + e

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""