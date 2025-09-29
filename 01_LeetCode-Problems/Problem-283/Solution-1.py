class Solution(object):
    def moveZeroes(self, nums):
        count = 1
        for i in nums:
            if nums == 0:
                count += 1
        for i in range(len(nums) - count):
            if i == 0:
                nums.remove(i)
                nums.append(0)
        
        return nums

sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))