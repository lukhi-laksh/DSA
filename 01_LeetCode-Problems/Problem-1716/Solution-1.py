class Solution:
    def totalMoney(self, n):
        weeks = n // 7
        days = n % 7
        lowest = 28
        highest = 28 + 7 * (weeks - 1)
        total = (lowest + highest) * weeks // 2

        monday = weeks + 1
        for i in range(days):
            total += i + monday
        
        return total