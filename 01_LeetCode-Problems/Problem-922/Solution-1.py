"""
Sort Array by Parity II

"""

class Solution:
    def sortArrayByParityII(self, nums):
        odd,even = [],[]
        for n in nums:
            if n%2: odd.append(n)
            else: even.append(n)
    
        o,e = 0,0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even[e]
                e+=1
            else:
                nums[i]=odd[o]
                o+=1
    
        return nums

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""