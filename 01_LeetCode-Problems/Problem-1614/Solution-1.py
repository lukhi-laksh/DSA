"""
Maximum Nesting Depth of the Parenthesis

"""
class Solution(object):
    def maxDepth(self, s):
        m=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append("(")
                m=max(m,len(stack))
            elif(i==")"):
                stack.pop()
        return m

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""