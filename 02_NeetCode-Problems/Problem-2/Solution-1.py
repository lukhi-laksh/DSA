class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1_list = list(s)
        str2_list = list(t)
        for i in str1_list:
            for j in str2_list:
                if (str1_list[i] != str2_list[j]):
                    False
        True


str1 = "laksh"
str2 = "hskal"
solutions = Solution()
print(solutions.isAnagram(str1, str2))