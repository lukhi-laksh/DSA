class Solution(object):
    def removeSubfolders(self, folder):

        folder.sort()
        res = []
        # For each
        for dir in folder:
            # Checking Condition
            if not res or not dir.startswith(res[-1] + '/'):
                res.append(dir)
        return res