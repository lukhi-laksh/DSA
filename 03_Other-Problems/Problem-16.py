class Solution(object):
    def removeSubfolders(self, folder):

        folder.sort()  # sort lexicographically
        res = []
        for dir in folder:
            if not res or not dir.startswith(res[-1] + '/'):
                res.append(dir)
        return res