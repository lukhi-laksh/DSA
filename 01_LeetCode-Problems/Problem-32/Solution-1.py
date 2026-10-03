"""
Longest Valid Parentheses

"""
class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        maximum = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    maximum = max(maximum, i - stack[-1])

        return maximum

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""