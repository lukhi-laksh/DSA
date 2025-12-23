"""
Rotate Array

"""


class Solution(object):
    def rotate(self, nums, k):

        k = k % len(nums)
        n = len(nums)
        start = 0
        count = 0 

        while count < n:
            cur_idx, prev = start, nums[start]

            while True:
                next_idx = (cur_idx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                cur_idx = next_idx 

                count += 1
                if cur_idx == start:
                    break
            
            start += 1
        
        return nums

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""