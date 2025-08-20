class solution():
    def twoSum(self, nums, target):
        ans = set()
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right:
            sum = nums[left] + nums[right]

            if (sum == target):
                ans.add((nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1
        
        return [list(t) for t in ans]

sol = solution()
nums = [2, 4, 6, 8, 10, 12]
target = 18
print(sol.twoSum(nums, target))