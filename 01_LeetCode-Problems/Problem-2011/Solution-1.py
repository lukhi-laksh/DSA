class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for s in operations:
            if(s[1]=='-'):
                x = x - 1
            else:
                x = x + 1
        
        return x