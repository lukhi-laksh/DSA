"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""
class Solution(object):
    def searchInsert(self, nums, target):
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
                

sol = Solution()
nums = [3, 5, 7, 9, 13]
target = 11

print(sol.searchInsert(nums, target))


"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""