"""
Smallest Index with Digit Sum Equal to Index

"""
class Solution(object):
    def smallestIndex(self, nums):

        for i in range(len(nums)):
            num=nums[i]
            summ=0
            while num>0:
                summ+=num%10
                num//=10
            if summ==i:
                return i
        return-1