"""
Valid Anagram

"""
class Solution(object):
    def isAnagram(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
    
sol =  Solution()
print(sol.isAnagram('laksh', 'shkal'))
"""
Time Complexity:  O(n log n)
Space Complexity: O(n)

"""