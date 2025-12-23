"""
Basic Calculator

"""

class Solution(object):
    def calculate(self, s):

        s = s.replace(' ', '')
        element_list = []
        operations = set(['+', '-', '*', '/'])
        L = len(s)
        left, right = 0, 0 


        for right in range(L):
            if s[right] in operations:
                element_list.append(int(s[left:right]))
                element_list.append(s[right])
                left = right+1

        if left < L:
            element_list.append(int(s[left:]))

        print(element_list)
        element_list = element_list

        self.stack = []
        k = 0
        while k < len(element_list):
            element = element_list[k]
            if element not in operations:
                self.stack.append(element)
                k+=1
            else:
                self.compute(element, element_list[k+1])
                k+=2

        return sum(self.stack)
            
    def compute(self, op, v):
        if op == '+':
            return self.stack.append(v)
        if op == '-':
            return self.stack.append(-v)
        if op == '*':
            return self.stack.append(self.stack.pop() * v)
        if op == '/':
            return self.stack.append(int(self.stack.pop() / float(v)))
        
"""
Time Complexity: O(n)
Space Complexity: O(n)

"""