"""
Zigzag Conversion

"""

class Solution(object):
    def convert(self, s, numRows):
        
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        flag = 1
        row = 0

        for char in s:
            rows[row] += char

            if row == 0:
                flag = 1
            elif row == numRows - 1:
                flag = -1

            row += flag
            
        return ''.join(rows)
    
"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""