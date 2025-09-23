class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")
        c = 0
        while c < len(version1) and c < len(version2):
            if int(version1[c])>int(version2[c]):
                return 1
            elif int(version2[c])>int(version1[c]):
                return -1
            else:
                c += 1
        if c < len(version1):
            for i in version1[c:]:
                if int(i) > 0:
                    return 1
        if c < len(version2):
            for i in version2[c:]:
                if int(i) > 0:
                    return -1
        return 0
    
sol = Solution()
version1 = "1.01"
version2 = "1.001"

print(sol.compareVersion(version1, version2))