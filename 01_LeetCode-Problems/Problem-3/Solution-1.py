"""
Given a string s, find the length of the longest substring without duplicate characters.

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
    
        length = len(s)
        max_length = 0
        longest_substr = ""
        for i in range(length):
            for j in range(i+1, length+1):
                subString = s[i:j]
                if len(subString) == len(set(subString)):
                    if len(subString) > max_length:
                        max_length = len(subString)
                        longest_substr = subString

        print("Longest substring with unique characters:", longest_substr)
        print("Size of the longest substring:", max_length)
        return max_length
            

sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))

"""
Time Complexity:  O(n³)
Space Complexity: O(k)

"""