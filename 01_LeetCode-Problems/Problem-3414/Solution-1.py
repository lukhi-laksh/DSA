"""
Maximum Score of Non-Overlapping Intervals

"""
class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        A = []
        for i in range(n):
            A.append([intervals[i][0], intervals[i][1], intervals[i][2], i])
            
        A.sort()
        
        next_idx = [n] * n
        for i in range(n):
            target = A[i][1] + 1
            low, high = i + 1, n
            while low < high:
                mid = (low + high) // 2
                if A[mid][0] >= target:
                    high = mid
                else:
                    low = mid + 1
            next_idx[i] = low

        def get_best(res1, res2):
            w1, idxs1 = res1
            w2, idxs2 = res2
            if w1 != w2:
                return res1 if w1 > w2 else res2
            return res1 if idxs1 < idxs2 else res2

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            start, end, weight, orig_idx = A[i]
            nxt = next_idx[i]
            
            for count in range(1, 5):
                skip_res = dp[i + 1][count]
                
                next_w, next_idxs = dp[nxt][count - 1]
                
                take_idxs = [orig_idx] + next_idxs
                take_idxs.sort() 
                
                take_res = (weight + next_w, take_idxs)
                
                dp[i][count] = get_best(skip_res, take_res)
                
        return dp[0][4][1]

"""
Time Complexity(n log n)
Space Complexity(n)

"""