"""
Alice and Bob Playing Flower Game

"""
class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        odd1 = (n + 1) // 2
        even1 = n // 2

        odd2 = (m + 1) // 2
        even2 = m // 2

        return odd1 * even2 + odd2 * even1
    
sol = Solution()
print(sol.flowerGame(2, 3))
    
"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""