class Solution(object):
    def findComplement(self, num):
        complement = ""
        for i in bin(num)[2:]:
            if i == "0":
                complement += "1"
            else:
                complement += "0"
        return int(complement, 2)


sol = Solution()
print(sol.findComplement(5))
