from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            grouped[key].append(word)

        return list(grouped.values())

sol = Solution()
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(sol.groupAnagrams(strs))