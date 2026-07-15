"""
GCD of Odd and Even Sums

"""
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        oddsum = n * n
        evensum = n * (n + 1)

        while evensum:
            oddsum, evensum = evensum, oddsum % evensum

        return oddsum
    
"""
Time Complexity: O(log(min(oddsum, evensum)))
Space Complexity: O(1)

"""