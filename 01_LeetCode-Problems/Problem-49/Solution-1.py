"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

"""
class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) < 1:
            return [""]
        if len(strs) < 2:
            return [strs]
        empty = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in empty:
                empty[key] = []
            empty[key].append(word)
        return list(empty.values())

    
sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))


"""
Time Complexity:   O(n * k log k)
Space Complexity:  O(n * k)

"""