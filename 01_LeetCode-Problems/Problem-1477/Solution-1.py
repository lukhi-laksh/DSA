"""
Find Two Non-overlapping Sub-array Each With Target Sum

"""
class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        best = [INF] * n
        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                best[right] = length
            if right > 0:
                best[right] = min(best[right], best[right - 1])

        return -1 if ans == INF else ans

"""
Time Complexity: O(n log n)
Space Complexity: O(1)

"""