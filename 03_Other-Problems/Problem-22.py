class solution():
    def FourSum(self, nums, target):
        n = len(nums)
        ans = set()
        # Takes two values one by one
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                start = j + 1
                end = n - 1

                # Binary search
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]

                    # Check sum with target
                    if sum == target:
                        ans.add((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                    elif sum < target:
                        start += 1
                    else:
                        end -= 1
        return [list(t) for t in ans]

sol = solution()
nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
target = 40
print(sol.FourSum(nums, target))
