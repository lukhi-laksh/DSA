"""
Maximum number of operations to Move Ones to the end

"""

class Solution(object):
    def maxOperations(self, s):
        ans, cum = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                cum += 1
            elif i > 0 and s[i] == '0' and s[i-1] == '1':
                ans += cum
        return ans
    
"""

Time Complexity:  O(n)
Space Complexity: O(1)

"""