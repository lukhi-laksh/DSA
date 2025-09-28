"""
Find all duplicates in array

"""
class Solution(object):
    def findDuplicates(self, nums):
        lst=[]
        for i in range(len(nums)):
            n=abs(nums[i])
            if nums[n-1]<0:
                lst.append(n)
            else:
                nums[n-1]=nums[n-1]*-1
        return lst

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""