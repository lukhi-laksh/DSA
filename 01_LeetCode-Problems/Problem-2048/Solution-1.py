from collections import Counter

def Check(x):
    for num, count in Counter(str(x)).items():
        if num != str(count):
            return False
    return True

Bal_Nums = []
for i in range(1224445):
    if Check(i):
        Bal_Nums.append(i)

class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = len(Bal_Nums) - 1
        res = Bal_Nums[-1]
        
        while l <= r:
            m = (l + r) // 2
            if Bal_Nums[m] > n:
                res = Bal_Nums[m]
                r = m - 1
            else:
                l = m + 1
        
        return res