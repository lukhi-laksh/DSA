"""
Minimum number of pushes to Type Word I

"""
class Solution(object):
    def minimumPushes(self, word):
        count = 0
        for i in range(len(word)):
            count += i // 8 + 1
        return count

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""