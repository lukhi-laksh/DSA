class Solution:
    def uniformArray(self, nums1):
        odd = sum(x & 1 for x in nums1)
        even = len(nums1) - odd

        all_even = (odd == 0) or (odd >= 2)

        all_odd = (even == 0) or (odd >= 1)

        return all_even or all_odd