"""
Valid Anagram

"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in t:
                t = t.replace(i, '', 1)
            else:
                return False
        return True
        
sol = Solution()
print(sol.isAnagram('anagram', 'nagaram'))

"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""