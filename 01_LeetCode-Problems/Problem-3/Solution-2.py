"""
Given a string s, find the length of the longest substring without duplicate characters.

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        max_length = 0
        longest_substr = ""

        for i in range(length):
            seen = set()
            for j in range(i, length):
                if s[j] in seen:
                    break
                seen.add(s[j])
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    longest_substr = s[i:j+1]

        print("Longest substring with unique characters:", longest_substr)
        print("Size of the longest substring:", max_length)
        return max_length

# Test
sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))

"""
Time Complexity: O(n²)
Space Complexity: O(k)

"""