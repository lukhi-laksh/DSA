class Solution(object):
    def maxFrequencyElements(self, nums):
        SetNums = set(nums)
        frequency = 0
        count = 0

        for i in SetNums:
            temp_freq = nums.count(i)
            if frequency == temp_freq:
                count += 1
            elif frequency < temp_freq:
                frequency = temp_freq
                count = 1
        return frequency * count

sol = Solution()
print(sol.maxFrequencyElements([1, 2, 3, 4, 5]))