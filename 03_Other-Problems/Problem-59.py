class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x // 2 + 1

        while l < r:
            mid = (l + r) // 2

            if(mid * mid > x):
                r = mid
            else:
                l = mid + 1 

        return x if x == 0 or x == 1 else l - 1

sol = Solution()
print(sol.mySqrt(6))