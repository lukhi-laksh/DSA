"""
Count Odd Numbers In an Interval Range

"""

class Solution(object):
    def countOdds(self, low, high):
        a=(high-low)//2
        if high%2==1 or low%2==1:
            a+=1
        return a
    
"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""
        