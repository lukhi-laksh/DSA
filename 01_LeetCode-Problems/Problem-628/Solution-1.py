"""
Maximum Product of Three Numbers

"""
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort();
        if(nums[0]<0 and nums[1]<0):
            if(nums[0]*nums[1]*nums[-1]>nums[-1]*nums[-2]*nums[-3]):
                return nums[0]*nums[1]*nums[-1]
        return nums[-1]*nums[-2]*nums[-3]

"""
Time Complexity:  O(1)
Space Complexity: O(1)

"""