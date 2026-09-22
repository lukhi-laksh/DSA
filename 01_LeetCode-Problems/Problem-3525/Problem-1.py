class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        size = 1
        while size < n:
            size *= 2

        tree_prod = [1] * (2 * size)
        tree_cnt = [[0] * k for _ in range(2 * size)]

        # build leaves
        for i in range(n):
            p = nums[i] % k
            tree_prod[size + i] = p
            tree_cnt[size + i][p] = 1

        # build tree
        for i in range(size - 1, 0, -1):
            self.merge(i, 2 * i, 2 * i + 1, tree_prod, tree_cnt, k)

        def update(pos, val):
            i = size + pos
            tree_prod[i] = val % k
            tree_cnt[i] = [0] * k
            tree_cnt[i][tree_prod[i]] = 1

            i //= 2
            while i:
                self.merge(i, 2 * i, 2 * i + 1, tree_prod, tree_cnt, k)
                i //= 2

        def query(l, r):
            left_prod, right_prod = 1, 1
            left_cnt = [0] * k
            right_cnt = [0] * k

            l += size
            r += size

            while l <= r:
                if l % 2 == 1:
                    left_prod, left_cnt = self.combine(left_prod, left_cnt, tree_prod[l], tree_cnt[l], k)
                    l += 1
                if r % 2 == 0:
                    right_prod, right_cnt = self.combine(tree_prod[r], tree_cnt[r], right_prod, right_cnt, k)
                    r -= 1
                l //= 2
                r //= 2

            final_prod, final_cnt = self.combine(left_prod, left_cnt, right_prod, right_cnt, k)
            return final_cnt

        res = []

        for idx, val, start, x in queries:
            update(idx, val)
            cnt = query(start, n - 1)
            res.append(cnt[x])

        return res

    def merge(self, i, l, r, tree_prod, tree_cnt, k):
        lp, rp = tree_prod[l], tree_prod[r]
        tree_prod[i] = (lp * rp) % k

        new_cnt = [0] * k
        for a in range(k):
            new_cnt[a] += tree_cnt[l][a]
        for b in range(k):
            if tree_cnt[r][b]:
                new_cnt[(lp * b) % k] += tree_cnt[r][b]

        tree_cnt[i] = new_cnt

    def combine(self, p1, c1, p2, c2, k):
        if sum(c1) == 0:
            return p2, c2
        if sum(c2) == 0:
            return p1, c1

        new_p = (p1 * p2) % k
        new_c = [0] * k

        for i in range(k):
            new_c[i] += c1[i]

        for j in range(k):
            if c2[j]:
                new_c[(p1 * j) % k] += c2[j]

        return new_p, new_c