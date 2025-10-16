"""
Smallest Missing Non-Negative Integer After Operations

"""
class Solution(object):
    def findSmallestInteger(self, nums, value):
        freq = [0] * value
        for num in nums:
            x = ((num % value) + value) % value
            freq[x] += 1
        
        j = 0
        while True:
            x = j % value
            if freq[x] == 0:
                return j
            freq[x] -= 1
            j += 1


"""

Time Complexity:  O(n)
Space Complexity: O(n)

"""