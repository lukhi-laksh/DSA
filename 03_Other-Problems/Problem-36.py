class Solution(object):
    def minOperations(self, queries):

        def steps(x):
            if x == 0:
                return 0
            e = 0
            while 4 ** e <= x:
                e += 1
            return e  
        
        total = 0
        for l, r in queries:
            sum_steps = 0
            max_k = steps(r)
            k = 1
            while True:
                start = 4 ** (k - 1)
                end = (4 ** k) - 1
                if start > r:
                    break
                if end < l:
                    k += 1
                    continue
                lower = max(l, start)
                upper = min(r, end)
                if lower > upper:
                    k += 1
                    continue
                count = upper - lower + 1
                sum_steps += count * k
                k += 1
                if k > max_k:
                    break
            max_ops = max_k
            sum_ops = (sum_steps + 1) // 2
            ops = max(max_ops, sum_ops)
            total += ops
        return total