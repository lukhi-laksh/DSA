"""
Binary Prefix Divisible By 5

"""

class Solution(object):
    def prefixesDivBy5(self, nums):
        e=[]
        s=""
        for i in range(len(nums)):
            s+=str(nums[i])
            d=int(s,2)
            e.append(d%5==0)
        return e

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""