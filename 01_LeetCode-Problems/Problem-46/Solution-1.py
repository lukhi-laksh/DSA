"""
Permutations

"""


class Solution(object):
    def permute(self, nums):

        if len(nums) == 1:
            return [nums]
        
        res = []
        def back(path,rem):
            if rem == []:
                res.append(path[:])
                return
            
            for i in range(len(rem)):
                path.append(rem[i])
                tmp = rem.pop(i)
                back(path,rem)
                path.pop()
                rem.insert(i,tmp)
        
        back([],nums)
        return res

"""
Time Complexity: O(n!)
Space Complexity: O(n)

"""