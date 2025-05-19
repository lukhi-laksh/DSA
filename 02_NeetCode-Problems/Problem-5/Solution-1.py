from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        # Sort the dictionary by frequency in descending order
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        
        # Extract the top k elements
        l = []
        for i in range(k):
            l.append(sorted_items[i][0])
        
        return l
    
sol = Solution()
nums = [-1, -1]
k = 1
print(sol.topKFrequent(nums, k))