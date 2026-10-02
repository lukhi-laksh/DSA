class Solution:
    def generateParenthesis(self, n):
        ans = []

        def solve(open_count, close_count, temp):

            if open_count == n and close_count == n:
                ans.append(temp)
                return

            if open_count < n:
                solve(open_count + 1, close_count, temp + '(')

            if close_count < open_count:
                solve(open_count, close_count + 1, temp + ')')

        solve(0, 0, "")

        return ans