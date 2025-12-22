"""
Evolute Reverse Polish Notation

"""

import numpy as np
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        ops = set(["+", "-", "*", "/"])
        ans = 0
        for token in tokens:
            if token in ops:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
     
                if token == "+":
                    res = n1 + n2
                elif token == "-":
                    res = n1 - n2
                elif token == "*":
                    res = n1 * n2
                elif token == '/':
                    res = (abs(n1) // abs(n2)) * np.sign(n1*n2)
                stack.append(res)
            else:
                stack.append(token)
            #print(stack)
        return int(stack[-1])

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""
        