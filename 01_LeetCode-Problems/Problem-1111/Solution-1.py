"""
Maximum Nesting Depth of Two Valid Parentheses Strings

"""
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        ans = []
        count = 0

        for ch in seq:
            if ch == '(':
                count += 1
                ans.append(count % 2)
            else:
                ans.append(count % 2)
                count -= 1

        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""