"""
Minimum Number of Changes to Make Binary String Beautiful

"""
class Solution(object):
    def minChanges(self, s):
        c=0
        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:
                c+=1
        return c

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""