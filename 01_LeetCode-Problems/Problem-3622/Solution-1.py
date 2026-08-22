"""
Check Divisibility by Digit Sum and Product

"""
class Solution:
    def checkDivisibility(self, n):

        original = n
        total_sum = 0
        product = 1

        while n > 0:

            digit = n % 10

            total_sum += digit
            product *= digit

            n //= 10

        return original % (total_sum + product) == 0

"""
Time Complexity: O(n log n)
Space Complexity: O(1)

"""