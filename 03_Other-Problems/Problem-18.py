class Solution(object):
    def convert(self, s, numRows):
        
        if numRows == 1 or len(s) < numRows:
            return s
        
        fi = [''] * numRows
        count = 1
        index = 0
        
        for char in s:
            fi[index] += char
            
            if index == 0:
                count = 1
            elif index == numRows - 1:
                count = -1
            
            index += count
        
        return ''.join(fi)
                

sol = Solution()
s = "LAKSHLUKHINARESHBHAI"
numRows = 4
print(sol.convert(s, numRows))
    