"""
Count Square Sum Triples

"""

class Solution(object):
    def countTriples(self, n):
        count = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                for k in range(j, n+1):
                    if i*i + j*j==k*k:
                        count += 2
        return count

"""
Time Complexity: O(n³)
Space Complexity: O(1)

"""