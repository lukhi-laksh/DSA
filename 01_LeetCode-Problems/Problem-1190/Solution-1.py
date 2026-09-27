"""
Reverse Substrings Between Each Pair of Parentheses

"""
class Solution(object):
    def reverseParentheses(self, s):

        stack = [""]
        
        for ch in s:

            if ch == '(':
                stack.append("")

            elif ch == ')':
                temp = stack.pop()
                stack[-1] += temp[::-1]

            else:
                stack[-1] += ch

        return stack[0]

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""