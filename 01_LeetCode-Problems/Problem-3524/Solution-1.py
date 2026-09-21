"""
Find X value of Array I

"""
class Solution():
    def resultArray(self, nums, k):
        n = len(nums)


        dp = [0] * k

        result = [0] * k

        for num in nums:
            x = num % k

            new_dp = [0] * k

            new_dp[x] += 1

            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * x) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            for r in range(k):
                result[r] += dp[r]

        return result

"""
Time Complexity: O(n * k)
Space Complexity: O(k)

"""