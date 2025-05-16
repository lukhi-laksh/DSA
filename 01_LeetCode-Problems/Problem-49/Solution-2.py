class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) < 1:
            return [""]
        if len(strs) < 2:
            return [strs]
        
        temp = []
        ans = []
        
        for i in range(len(strs)):
            x = sorted(strs[i])
            if x in temp:
                ans[temp.index(x)].append(strs[i])
            else:
                temp.append(x)
                ans.append([])
                ans[temp.index(x)].append(strs[i])
        
        return ans

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))

"""
Time Complexity:   O(n^2 * k + n * k log k)
Space Complexity:  O(n * k)

"""