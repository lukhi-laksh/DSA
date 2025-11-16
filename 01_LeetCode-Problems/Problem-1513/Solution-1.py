"""
Number of Substrings with only 1s

"""

class Solution(object):
    def numSub(self, s):

        MOD = 10**9 + 7
        n = len(s)
        j = 1
        answer = 0
        for i in range(n):
            if s[i] != '1':
                continue
            j = max(i + 1, j)
            while j < n and s[j] == '1':
                j += 1
            answer += (j - i)

        return answer % MOD
    
"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""
       