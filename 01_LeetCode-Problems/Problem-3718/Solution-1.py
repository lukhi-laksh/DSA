"""
Smallest Missing Multiple of K

"""
class Solution(object):
    def missingMultiple(self, nums, k):
        
        i = 1
        while True:
            if (i * k) not in nums:
                return (i * k)
            i += 1

"""
Time Complexity: O(n log n)
Space Complexity: O(1)

"""