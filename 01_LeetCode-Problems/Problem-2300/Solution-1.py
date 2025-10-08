"""
Sucessfull Pair of Spells and Potions

"""
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        sum = []
        for i in spells:
            temp = 0
            for j in potions:
                if i * j >= success:
                    temp += 1
            sum.append(temp)
        return sum

sol = Solution()
print(sol.successfulPairs([2], [8,5,8], 16))

"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""