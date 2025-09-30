"""
Find Triangular Sum of an Array

"""
class Solution(object):
    def triangularSum(self, nums):
        l=len(nums)
        while(l!=1):
            l=l-1
            for i in range(l):
                nums[i]=(nums[i]+nums[i+1])%10
        return nums[0]

sol = Solution()
print(sol.triangularSum([1, 2, 3, 4, 5]))


"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""