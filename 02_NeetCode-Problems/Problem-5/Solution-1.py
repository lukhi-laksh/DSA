from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        empty = [0] * (sorted_nums[-1] + 1)
        if len(sorted_nums) == 1:
            return nums
        elif sorted_nums[1] < 0:
            return -1
        else:
            for one in sorted_nums:
                empty[one] += 1

            top_k_indices = sorted(range(len(empty)), key=lambda i: empty[i], reverse=True)[:k]
    
            return top_k_indices


        
sol = Solution()
nums = [-1, -1]
k = 1
print(sol.topKFrequent(nums, k))