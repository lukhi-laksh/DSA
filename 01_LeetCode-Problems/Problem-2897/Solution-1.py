"""
Apply Operations on Array to Maximize Sum of Squares

"""
class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        cnt = [0] * 30

        for x in nums:
            for b in range(30):
                if x >> b & 1:
                    cnt[b] += 1

        ans = 0
        for _ in range(k):
            x = 0
            for b in range(30):
                if cnt[b]:
                    x |= 1 << b
                    cnt[b] -= 1
            ans = (ans + x * x) % MOD

        return ans

"""
Time Complexity: O(n + k)
Space Complexity: O(1)

"""