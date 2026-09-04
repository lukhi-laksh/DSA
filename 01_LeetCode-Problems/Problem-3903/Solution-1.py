"""
Smallest Stable Index I

"""
class Solution(object):
    def firstStableIndex(self, nums, k):
        maxi=[nums[0]]
        for i in nums[1:]:
            if(i>maxi[-1]):
                maxi.append(i)
            else:
                maxi.append(maxi[-1])
        mini=[nums[-1]]
        for i in nums[:-1][::-1]:
            if(i<mini[-1]):
                mini.append(i)
            else:
                mini.append(mini[-1])
        mini=mini[::-1]
        for i in range(len(nums)):
            if(maxi[i]-mini[i]<=k):
                return i
        return -1

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""