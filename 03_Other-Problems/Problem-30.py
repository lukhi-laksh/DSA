class Solution(object):
    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        laksh = 1  # start with 1, since 1 is always a divisor
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                laksh += i
                if i != num // i:
                    laksh += num // i
        return laksh == num

sol = Solution()
print(sol.checkPerfectNumber(28))