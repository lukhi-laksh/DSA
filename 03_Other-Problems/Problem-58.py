class Solution(object):
    def containsDuplicate(self, nums):

        empty = set()
        for i in nums:
            if i in empty:
                return True
            else:
                empty.add(i)
        return False
            
    
sol = Solution()
nums = [2, 3, 4, 6]
print(sol.containsDuplicate(nums))
