import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = list(s)
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        k = len(s)

        for i in range(k // 2):
            if (s[i] != s[k-i-1]):
                return False
        return True


sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw"))