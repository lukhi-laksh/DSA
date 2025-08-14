"""
Code
Testcase
Test Result
Test Result


2264. Largest 3-Same-Digit Number in String
Easy
Topics
premium lock icon
Companies
Hint
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
"""

class Solution(object):
    def largestGoodInteger(self, num):
        arr = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
        for i in arr:
            if i in num:
                return i
        return ""

sol = Solution()
num = '42352338'
print(sol.largestGoodInteger(num))
            
        
"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""