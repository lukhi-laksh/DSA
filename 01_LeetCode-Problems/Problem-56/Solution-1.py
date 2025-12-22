"""
Merge Intervals

"""


class Solution(object):
    def merge(self, nums):
        nums=sorted(nums, key=lambda x: x[0])
        l=nums[0][0]
        r=nums[0][1]
        n=len(nums)
        ans=[]
        for i in range(1,n):
            curr_l=nums[i][0]
            curr_r=nums[i][1]
            if r>=curr_l:
                r=max(curr_r,r)
            else:
                print(l,r)
                ans.append([l,r])
                l,r=curr_l,curr_r
        ans.append([l,r])
        return ans
    
"""
Time Complexity: O(n log n)
Space Complexity: O(n)

"""
