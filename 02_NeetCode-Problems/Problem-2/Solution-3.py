class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CountS = {}
        CountT = {}

        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)

        print(CountS)
        print(CountT)

        return CountS == CountT
           


sol = Solution()
s = "llaksh"
t = "aklsha"
print(sol.isAnagram(s, t))