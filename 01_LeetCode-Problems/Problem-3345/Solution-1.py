"""
Smallest Divisible Digit Product I

"""
class Solution(object):
    def smallestNumber(self, n, t):

        num = n

        while True:
            temp = num
            product = 1

            while temp > 0:
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                return num

            num += 1


"""

Time Complexity:  O(n)
Space Complexity: O(1)

"""