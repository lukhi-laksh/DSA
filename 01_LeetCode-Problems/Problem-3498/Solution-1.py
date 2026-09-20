"""
Reverse Degree of a String

"""
class Solution(object):

    def reverseDegree(self, s):

        res = 0

        for i in range(len(s)):
            res += (i + 1) * (26 - (ord(s[i]) - ord('a')))

        return res

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""