"""
Check if all 1's are at Least Leangth K places Away

"""

class Solution(object):
    def kLengthApart(self, nums, k):

        indices = [i for i,x in enumerate(nums) if x == 1 ]
        print(indices)
        
        for i in range(1, len(indices)):
            if (indices[i]-indices[i-1]-1) < k:
                return False
        return True
    
sol = Solution()
print(sol.kLengthApart([1,0,0,0,1,0,0,1], 2))

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""