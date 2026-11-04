"""
Minimum Operations to Make Elements Within K Subarrays Equal

"""

class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)

        values = sorted(set(nums))
        m = len(values)

        rank = {v: i + 1 for i, v in enumerate(values)}

        count_tree = [0] * (m + 1)
        sum_tree = [0] * (m + 1)

        def update(tree, i, delta):
            while i <= m:
                tree[i] += delta
                i += i & -i

        def query(tree, i):
            result = 0
            while i > 0:
                result += tree[i]
                i -= i & -i
            return result

        def kth(k):
            idx = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                nxt = idx + bit

                if nxt <= m and count_tree[nxt] < k:
                    idx = nxt
                    k -= count_tree[nxt]

                bit >>= 1

            return idx + 1

        total_sum = 0

        for i in range(x):
            v = nums[i]
            r = rank[v]

            update(count_tree, r, 1)
            update(sum_tree, r, v)
            total_sum += v

        costs = []

        for start in range(n - x + 1):
            median_rank = kth((x + 1) // 2)
            median = values[median_rank - 1]

            left_count = query(count_tree, median_rank)
            left_sum = query(sum_tree, median_rank)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            if start + x < n:
                old = nums[start]
                new = nums[start + x]

                update(count_tree, rank[old], -1)
                update(sum_tree, rank[old], -old)

                update(count_tree, rank[new], 1)
                update(sum_tree, rank[new], new)

                total_sum += new - old

        prev = [0] * (n + 1)

        for _ in range(1, k + 1):
            curr = [float('inf')] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]

"""
Time Complexity: O(n log n + n*k)
Space Complexity: O(n)
"""