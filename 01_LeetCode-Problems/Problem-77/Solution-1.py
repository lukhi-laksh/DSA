"""
Combinations

"""


class Solution(object):
    def combine(self, n, k):
        res = []
        path = []

        def backtrack(i):
            if len(path) == k:
                res.append(path[:])
            
            for m in range(i,n+1):
                path.append(m)
                backtrack(m+1)
                path.pop()
        
        backtrack(1)
        return res

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""