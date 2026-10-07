"""
Remove Invalid Parentheses

"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
            valid = []
            for s in level:
                try:
                    eval('0,' + filter('()'.count, s).replace(')', '),'))
                    valid.append(s)
                except:
                    pass
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

"""
Time Complexity: O(n².n)
Space Complexity: O(n².n)

"""