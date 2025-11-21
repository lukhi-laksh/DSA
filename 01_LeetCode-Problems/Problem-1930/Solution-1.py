"""
Unique Length-3 Pelindromic Subsequences

"""
from typing import Counter


class Solution(object):
    def countPalindromicSubsequence(self, s):

        res=set()
        left=set()
        c=Counter(s)

        for n in s:
            c[n]-=1
            for l in left:
                if c[l]>0:
                    res.add((n,l))
                
            left.add(n)
        
        return len(res)
    
"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""