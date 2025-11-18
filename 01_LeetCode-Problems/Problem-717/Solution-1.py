"""
1-bit and 2-bit Characters

"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        new_list  = []
        i = 0
        n = len(bits)
        while i < n:
            if bits[i] == 0:
                new_list.append(0)
                i += 1
            else:
                new_list.append(10)
                i+=2
        return new_list[-1] == 0            
       
"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""