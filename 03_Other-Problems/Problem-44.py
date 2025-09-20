
def gcd(a, b):
    while b:
        a,b=b,a%b
    return a


def lcm(a,b):
    return (a*b)//gcd(a,b)


class Solution(object):
    def replaceNonCoprimes(self, nums):
        s=[] 
        for i in nums:
            while s and gcd(s[-1],i)>1: 
                i=lcm(s.pop(),i) 
            s.append(i) 
        return s 