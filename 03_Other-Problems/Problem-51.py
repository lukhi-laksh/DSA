class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        ansmaker = ""
        if numerator == 0:
            return "0"
        if numerator<0 and denominator<0:
            numerator = -1*numerator
            denominator = -1*denominator
        elif numerator<0 and denominator>=0:
            numerator = -1*numerator
            ansmaker= "-"
        elif numerator>=0 and denominator<0:
            denominator = -1* denominator
            ansmaker = "-"
        dict1 = {}
        q = numerator//denominator
        r = numerator%denominator
        # print(q,r)
        if r == 0:
            return(ansmaker + str(q))
        else:
            ans = ansmaker+ str(q) + "."
        while True:
            if r == 0:
                return ans
            if r in dict1:
                sl = dict1[r]
                ans = ans[:sl] + "(" + ans[sl:] + ")"
                return ans
            dict1[r] = len(ans)
            r = r*10
            q = r//denominator
            r = r%denominator
            ans = ans+str(q)

sol = Solution()
print(sol.fractionToDecimal(0.1, 2))