"""
Restore IP Address

"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        def dfs(start, digits):
            if start == len(s):
                if len(digits) == 4:
                    result.append(".".join(digits[:]))
                return
            for i in range(start, min(start+3, len(s))):
                digit = s[start:i + 1]
                if (digit[0] == "0" and len(digit) > 1) or int(digit) > 255:
                    continue
                digits.append(digit)
                dfs(i+1, digits)
                digits.pop()
        dfs(0, [])
        return result

"""
Time Complexity: O(3ⁿ)
Space Complexity: O(n)

"""

