"""
Find x-sum of all K-long Subarrays I

"""
def Su(arr,x):
    temp = []
    su = 0
    se = set(arr)
    if len(se) <= x:
        return sum(arr)
    for s in se:
        temp.append((s,arr.count(s)))
    temp = sorted(temp, key=lambda x: (x[1], x[0]), reverse=True)
    for i in range(x):
        su +=  (temp[i])[0] * (temp[i])[1]
    return su

class Solution(object):
    def findXSum(self, nums, k, x):
        res = []
        l = len(nums)
        for i in range(l-k+1):
            res.append(Su(nums[i:i+k],x))
        return res
    
    
"""

Time Complexity:  O(n⋅(k2+klogk))
Space Complexity: O(k)

"""