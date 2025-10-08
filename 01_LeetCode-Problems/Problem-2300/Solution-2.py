"""
Sucessfull Pair of Spells and Potions

"""
class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(potions)
        ans = []

        for spell in spells:
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if spell * potions[mid] >= success:
                    high = mid - 1
                else:
                    low = mid + 1
            ans.append(n - low)
        
        return ans
    

sol = Solution()
print(sol.successfulPairs([2], [8,5,8], 16))

"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""