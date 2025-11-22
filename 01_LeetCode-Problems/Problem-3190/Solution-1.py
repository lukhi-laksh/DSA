"""
Find Minimum Operation to Make all Elements Divisable by Three

"""

class Solution(object):
    def minimumOperations(self, nums):
        res=0
        for i in nums:
            if (i+1)%3==0 or (i-1)%3==0:
                res+=1
        return res

"""

Time Complexity:  O(n)
Space Complexity: O(1)

"""