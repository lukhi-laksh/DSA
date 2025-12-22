"""
Combination Sum

"""

class Solution(object):
    def combinationSum(self, candidates, target):
        resp = set()
        def backtrack(curr, t):
            if t == 0:
                curr.sort()
                resp.add(tuple(curr))
                return
            exist = False
            for n in candidates:
                if n <= t:
                    exist = True
                    backtrack(curr + [n], t - n)
            if not exist and t != 0:
                return

        backtrack([], target)
        return list(resp)
    
"""
Time Complexity: O(2ⁿ)
Space Complexity: O(n)

"""
        