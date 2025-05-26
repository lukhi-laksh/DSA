class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CountS = {}
        CountT = {}

        for i in s:
           if i in CountS:
               CountS[i] += 1
           else:
               CountS[i] = 1

        for j in t:
           if j in CountT:
               CountT[j] += 1
           else:
               CountT[j] = 1

        print(CountS)
        print(CountT)

        if CountS == CountT:
            return True
        return False



sol = Solution()
s = "laaksh"
t = "aklsha"
print(sol.isAnagram(s, t))