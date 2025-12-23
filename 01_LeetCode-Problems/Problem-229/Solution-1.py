"""
Majority Element

"""


from typing import Counter


class Solution(object):
    def majorityElement(self, nums):
        ref=Counter(nums)
        n=len(nums)
        ans=[]
        for i,j in ref.items():
            if j>n/3:
                ans.append(i)
        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""

        