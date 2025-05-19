from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in empty:
                empty[key] = []
            empty[key].append(word)

        return list(empty.values())


sol = Solution()
words = ["act", "pots", "tops", "cat", "stop", "hat"]
print(sol.groupAnagrams(words))
