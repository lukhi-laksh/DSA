"""
Duplicates Zeros

"""

class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        l=len(arr)
        while i<l:
            if arr[i]==0:
                arr.insert(i+1,0)
                i+=1
                arr.pop()
            i+=1

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""