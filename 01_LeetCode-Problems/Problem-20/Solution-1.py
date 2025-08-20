"""
Valid Parentheses
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif i == ')':
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif i == '}':
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
            


sol = Solution()
s = "({}()"
print(sol.isValid(s))

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""