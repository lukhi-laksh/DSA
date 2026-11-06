"""
Count Zero Request Servers

"""
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        q = sorted((t, i) for i, t in enumerate(queries))

        count = [0] * (n + 1)
        ans = [0] * len(queries)

        left = right = active = 0
        total = len(logs)

        for t, idx in q:
            start = t - x

            while right < total and logs[right][1] <= t:
                s = logs[right][0]

                if count[s] == 0:
                    active += 1

                count[s] += 1
                right += 1

            while left < right and logs[left][1] < start:
                s = logs[left][0]

                count[s] -= 1

                if count[s] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans