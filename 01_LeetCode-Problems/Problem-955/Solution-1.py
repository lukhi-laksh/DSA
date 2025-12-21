"""
Delete Columns to Make Sorted II

"""

class Solution(object):
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        sorted_ok = [False] * (n - 1)
        ans = 0

        for col in range(m):
            delete = False
            for i in range(n - 1):
                if not sorted_ok[i] and strs[i][col] > strs[i + 1][col]:
                    delete = True
                    break

            if delete:
                ans += 1
            else:
                for i in range(n - 1):
                    if strs[i][col] < strs[i + 1][col]:
                        sorted_ok[i] = True

        return ans
    
"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""