"""
Happy Number

"""
class Solution(object):
    def isHappy(self, n):
        storage = set()
        
        def sums(n):
            if n == 1:
                return True
            elif n in storage:
                return False
            else:
                storage.add(n)
                n = sum([int(i) ** 2 for i in str(n)])
                return sums(n)
        
        return sums(n)
                
        
sol = Solution()
print(sol.isHappy(7))

"""
Time Complexity:  O(log n)
Space Complexity: O(log n)

"""