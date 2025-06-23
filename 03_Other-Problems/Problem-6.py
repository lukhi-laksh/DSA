class Solution(object):
    def FindLarge(self, sarr):
        n = len(sarr)
        right = [n] * n
        stack1 = []
        for i in range(n):
            while stack1 and sarr[i] < sarr[stack1[-1]]:
                top = stack1.pop()
                right[top] = i
            stack1.append(i)
        print("Right:", right)

        left = [-1] * n
        stack2 = []
        for i in range(n - 1, -1, -1):
            while stack2 and sarr[i] < sarr[stack2[-1]]:
                top = stack2.pop()
                left[top] = i
            stack2.append(i)

        print("Left:", left)

        ans = []
        for i in range(n):
            store = sarr[i] * (right[i] - left[i] - 1)
            ans.append(store)
        return max(ans)

    def CandyCresh(self, Sarr):
        ans = 0
        empty = [0] * len(Sarr[0])
        for i in range(len(Sarr)):
            for j in range(len(Sarr[0])):
                if Sarr[i][j] == 1:
                    empty[j] += 1
                else:
                    empty[j] = 0
            print("Row {} histogram: {}".format(i, empty))
            ans = max(ans, self.FindLarge(empty))
        return ans


sol = Solution()
Sarr = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1]
]
print("Max Rectangle Area:", sol.CandyCresh(Sarr))
