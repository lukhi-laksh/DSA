class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

str1 = "laksh"
str2 = "hskal"
solutions = Solution()
print(solutions.isAnagram(str1, str2)) 