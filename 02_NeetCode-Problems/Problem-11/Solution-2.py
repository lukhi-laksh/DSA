import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if s == s[::-1]:
            return True
        return False

sol = Solution()
s = "Wassaw"
print(sol.isPalindrome(s))