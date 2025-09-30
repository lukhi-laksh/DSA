"""
To Lower case

"""
class Solution(object):
    def toLowerCase(self, s):
        strs = ''
        for char in s:
            temp = ord(char)
            if temp > 64 and temp < 91:
                temp = temp + 32
                strs = strs + chr(temp)
            else:
                strs = strs + char
        return strs
                

sol = Solution()
print(sol.toLowerCase('sdfSDFsdf'))

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""