"""
Evalute the Bracket Pairs of Strings

"""
class Solution(object):
    def evaluate(self, s, knowledge):
        d = dict(knowledge)
        res = []
        l = 0
        
        for r, x in enumerate(s):
            if x == '(':
                res.append(s[l:r])
                l = r + 1
            elif x == ')':
                key = s[l:r]
                res.append(d.get(key, '?'))
                l = r + 1
        
        res.append(s[l:])
        return ''.join(res)

"""
Time complexity: O(n)
Space complexity: O(n+m)

"""