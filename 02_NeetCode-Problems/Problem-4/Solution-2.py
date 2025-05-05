import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = list(s)
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        revert =  s[::-1]

        if s == revert:
            return True
        return False


sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))