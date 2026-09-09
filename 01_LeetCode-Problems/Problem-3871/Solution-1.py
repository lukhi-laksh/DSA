"""
Count Commas in Range II

"""
class Solution:
    def countCommas(self, n):
        if n < 1000:
            return 0

        power = 1000
        groups = 1

        while power <= n // 1000:
            power *= 1000
            groups += 1

        result = groups * (n - power + 1)
        current_power = 1000

        for i in range(1, groups):
            result += 999 * current_power * i
            current_power *= 1000

        return result