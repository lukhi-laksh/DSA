class Solution(object):
    def Isvalid(self, s):

        # Create Stack
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

# Create object
sol = Solution()
s = "({)}"
print(sol.Isvalid(s))
