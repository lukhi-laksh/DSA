"""
Isomorephic Strings

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        dictstr = {}
        mapped = set()

        for i in range(len(s)):
            if s[i] in dictstr:
                if dictstr[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapped:
                    return False
                dictstr[s[i]] = t[i]
                mapped.add(t[i])
        return True

                
sol = Solution()
print(sol.isIsomorphic('badc', 'baba'))

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""