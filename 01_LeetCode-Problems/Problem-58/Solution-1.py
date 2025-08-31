"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

"""
class Solution(object):
    def lengthOfLastWord(self, s):
        laksh = len(s)
        if laksh == 0:
            return 0
        sum = 0
        tail = len(s) - 1
        while tail > 0 and s[tail] == ' ':
            tail -= 1
        for i in range(tail, -1, -1):
            if s[i] == ' ':
                return sum
            sum += 1
        return sum

sol = Solution()
s = 'jhhkhk    '
print(sol.lengthOfLastWord(s))

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""