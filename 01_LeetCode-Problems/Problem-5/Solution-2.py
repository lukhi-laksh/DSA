"""
Given a string s, return the longest palindromic substring in s.

"""
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        max_length = 1
        strt_length = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    if len(substr) > max_length:
                        max_length = len(substr)
                        strt_length = i
        return s[strt_length:strt_length + max_length]

sol = Solution()
s = "ac"
print(sol.longestPalindrome(s)) 

"""
Time Complexity:  O(n³)
Space Complexity: O(n)

"""
