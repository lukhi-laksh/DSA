"""
Taking Maximum Energy From the Mystic Dungeon

"""
class Solution(object):
    def maximumEnergy(self, energy, k):
        n = len(energy)
        for i in range(n - k - 1, -1, -1):
            energy[i] += energy[i + k]
            
        return max(energy)

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""