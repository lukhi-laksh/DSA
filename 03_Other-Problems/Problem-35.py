class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        for ops in range(1, 61):
            target = num1 - ops * num2
            if target <= 0:
                continue
            if ops <= target and target <= ops * (1 << 60):
                if bin(target).count('1') <= ops <= target:
                    return ops
        
        return -1

sol = Solution()
print(sol.makeTheIntegerZero(10, 25))