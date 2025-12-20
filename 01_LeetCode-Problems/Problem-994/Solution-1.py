"""
Delete Columns to Make Sorted

"""

class Solution(object):
    def minDeletionSize(self, strs):
        st=0
        l=[]
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                l.append(strs[j][i])
            if str(l)!=str(sorted(l)):
                st+=1
            
            l=[]
        return st
    
"""
Time Complexity:  O(n²)
Space Complexity: O(1)

"""