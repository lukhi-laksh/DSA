"""
Shortest and Lexicographically Smallest Beautiful String

"""
class Solution(object):

    def shortestBeautifulSubstring(self, s, k):
        n = len(s)

        ans = ""
        subString = ""

        length = float('inf')
        count1 = 0

        for i in range(n):

            subString += s[i]

            count1 = count1 + 1 if s[i] == '1' else count1

            if count1 == k:

                while len(subString) > 1 and subString[0] == '0':
                    subString = subString[1:]

                if (len(subString) < length or
                    (len(subString) == length and
                     (ans == "" or subString < ans))):

                    ans = subString
                    length = len(subString)

                if subString[0] == '1':
                    count1 -= 1

                subString = subString[1:]

        return ans

"""

Time Complexity:  O(n²)
Space Complexity: O(n)

"""