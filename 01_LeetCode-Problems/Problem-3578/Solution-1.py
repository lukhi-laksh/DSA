"""
Count Partitions With Max-Min Difference at Most K

"""

class SortedList:
    def __init__(self):
        pass

    def add(self, value):
        raise NotImplementedError

    def remove(self, value):
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

class Solution(object):
    def countPartitions(self, nums, k):
        mod = 10**9 + 7

        n = len(nums)
        prefix = [0, 1]
        val = -1

        j = 0
        Window = SortedList()

        for i in range(n):

            Window.add(nums[i])

            while j <= i and Window[-1]-Window[0] > k:
                Window.remove(nums[j])            
                j+=1

            val = (prefix[-1] - prefix[j] + mod) %mod
            prefix.append((val + prefix[-1]) %mod)

        return val

"""
Time Complexity: O(n · log n)
Space Complexity: O(n)

"""

