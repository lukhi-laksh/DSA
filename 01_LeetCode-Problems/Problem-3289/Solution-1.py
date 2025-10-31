"""
The Two Sneaky Numbers of Digitvilly

"""

class Solution(object):
    def getSneakyNumbers(self, nums):
        freq = [0] * len(nums)
        res = []
        
        for num in nums:
            freq[num] += 1
        
        for i in range(len(freq)):
            if freq[i] == 2:
                res.append(i)
        
        return res
    
"""

Time Complexity:  O(n)
Space Complexity: O(n)

"""