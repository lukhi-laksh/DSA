class Solution(object):
    def maxFreqSum(self, s):

        d={}
        mv,mc=0,0
        a={'a','e','i','o','u'}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
        for key,value in d.items():
            if key in a:
                mv=max(mv,value)
            else:
                mc=max(mc,value)
        return mv+mc

sol = Solution()
print(sol.maxFreqSum('laksh'))