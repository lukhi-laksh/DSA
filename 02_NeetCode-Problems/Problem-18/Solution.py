class Solution(object):
    def Celibrity(self, Sarr):
        stack = []
        for i in range(len(Sarr)):
            stack.append(i)
        while len(stack) > 1:
            first = stack.pop()
            second = stack.pop()

            if (Sarr[first][second] and not(Sarr[second][first])):
                stack.append(second)
            elif not(Sarr[first][second] and (Sarr[second][first])):
                stack.append(first)
        
        if len(stack) == 0:
            return -1
        
        check = stack.pop()
        row = 0
        column = 0
        for j in range(len(Sarr)):
            row += Sarr[check][j]
            column += Sarr[j][check]

        if row == 0 and column == len(Sarr) - 1:
            return check
        else:
            return -1
                
                
            

sol = Solution()
Sarr = [
    [1, 1, 1], 
    [0, 0, 0],
    [1, 1, 1]
]
print(sol.Celibrity(Sarr))