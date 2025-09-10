"""
1295. Find Numbers with Even Number of Digits

"""
class Solution(object):
    def findNumbers(self, nums):
        ans = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                ans += 1
        return ans

sol = Solution()
print(sol.findNumbers([1, 2, 3323]))

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""
        