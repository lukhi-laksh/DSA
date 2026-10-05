"""
Score of Parentheses

"""
class Solution(object):
    def scoreOfParentheses(self, s):
        cur = 0
        isOpened = False
        res = 0
        for c in s:
            if c == '(':
                cur +=1
                isOpened = True
            else:
                cur -=1
                if isOpened :
                    isOpened = False
                    res += 2**cur
        return res

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""