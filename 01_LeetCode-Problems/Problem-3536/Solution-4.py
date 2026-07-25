"""
Maximum Product of Two Digits

"""
class Solution(object):
    def maxProduct(self, n):
        arr =[]

        for i in range(len(str(n))):
            arr.append(str(n)[i])     
        arr.sort()
        if len(arr) == 1:
            return arr[-1]
        else:
            return int(arr[-1])*(int(arr[-2]))   

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""