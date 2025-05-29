from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res , i = [], 0

        while i < (len(s)):
            j = i + 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
    
sol = Solution()

strs = ["first", "second", "Third", "fourth"]
print(sol.decode(sol.encode(strs)))


