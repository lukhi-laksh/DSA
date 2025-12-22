"""
Simplify Path

"""

class Solution(object):
    def simplifyPath(self, path):
        stack = []
        pathList = path.split("/")
        print(pathList)
        for path in pathList:
            if path == "" or path == ".": 
                continue 
            elif path == "..": 
                if stack:
                    stack.pop(-1)
            else: 
                stack.append(path)
        newPath = "/".join(stack)
        print(newPath)
        return "/" + newPath
    
"""
Time Complexity: O(n)
Space Complexity: O(n)

"""
