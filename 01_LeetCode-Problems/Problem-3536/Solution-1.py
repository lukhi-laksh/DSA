"""
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

"""
import math
class Solution(object):
    def maxProduct(self, n):
        empty = []
        str_n = str(n)
        k = len(str_n)
        result = math.ceil(k / 2)
             
        for i in range(k):
            for j in range(i + 1, k):
                product = int(str_n[i]) * int(str_n[j])
                empty.append(product)
        return max(empty)
        
sol = Solution()
n = 345674
print(sol.maxProduct(n))

"""
Time Complexity:  O(k^2)
Space Complexity: O(k^2)

"""