class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)

        left, right = 0, diff[0]

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        result = 0
        remaining = k

        for d in diff:
            reduction = min(d, level)
            result += reduction * reduction
            remaining -= max(0, d - level)

        for d in diff:
            if remaining == 0:
                break
            if d >= level:
                result -= 2 * level - 1
                remaining -= 1

        return result