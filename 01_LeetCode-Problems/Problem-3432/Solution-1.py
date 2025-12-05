"""
Count Partitions with Even Sum Difference

"""

class Solution(object):
    def countPartitions(self, nums):
        
        n = len(nums)
        arr = [0]*n
        a = 0
        for i in range(n):
            a += nums[i]
            arr[i] = a
        flag = True
        c = 0 
        for i in range(n):
            b = abs(arr[i] - arr[-1])
            main = b - arr[i]
            print(b)
            if main%2 == 0:
                flag = True
                c += 1 
            else:
                flag = False
                return 0
        return c  - 1
    

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""