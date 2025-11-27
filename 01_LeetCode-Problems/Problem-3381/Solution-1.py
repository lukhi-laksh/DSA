"""
Maximum Subarray Sum With Length Divisible by k

"""

class Solution(object):
    def maxSubarraySum(self, nums, k):


        prefix_sum = 0
        max_sum = float('-inf')
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0
        
        for i, num in enumerate(nums, 1):
            prefix_sum += num
            rem = i % k
            if min_prefix[rem] != float('inf'):
                max_sum = max(max_sum, prefix_sum - min_prefix[rem])
            min_prefix[rem] = min(min_prefix[rem], prefix_sum)
            
        return max_sum if max_sum != float('-inf') else 0

"""
Time Complexity: O(n)
Space Complexity: O(k)

"""