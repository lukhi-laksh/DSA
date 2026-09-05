class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        prefixMax = [0] * n
        suffixMin = [0] * n

        prefixMax[0] = nums[0]
        suffixMin[n - 1] = nums[n - 1]

        for i in range(1, n):
            j = n - 1 - i

            prefixMax[i] = max(prefixMax[i - 1], nums[i])
            suffixMin[j] = min(suffixMin[j + 1], nums[j])

        for i in range(n):
            if prefixMax[i] - suffixMin[i] <= k:
                return i

        return -1