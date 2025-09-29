"""
Happy Number

"""
class Solution(object):
    def isHappy(self, n):
        storage = set()
        storage.add(n)
        
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in storage:
                return False
            else:
                storage.add(n)
        return True

        
sol = Solution()
print(sol.isHappy(7))

"""
Time Complexity:  O(log n)
Space Complexity: O(log n)

"""