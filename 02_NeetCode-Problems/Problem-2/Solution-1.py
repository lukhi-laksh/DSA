"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

str1 = "laksh"
str2 = "hskal"
solutions = Solution()
print(solutions.isAnagram(str1, str2)) 

"""
Time Complexity: O(n log n)
Space Complexity: O(1)

"""