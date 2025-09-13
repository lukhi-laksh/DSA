class Solution(object):
    def sumZero(self, n):
        first_part = list(range(1, n))
        second_part = -sum(first_part)
        return first_part + [second_part]