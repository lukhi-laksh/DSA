"""
Maximum Running Time of N Computers

"""

class Solution(object):
    def maxRunTime(self, n, batteries):

        left, right = 0, sum(batteries) // n

        while left <= right:
            mid = (left + right)//2
            target = sum(min(b,mid) for b in batteries)
            
            if(target < mid * n):
                right = mid - 1
            else:
                left = mid + 1

        return right
    

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""

