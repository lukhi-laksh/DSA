"""
Split Array into Fibonacci Sequence

"""

class Solution:
    def splitIntoFibonacci(self, num):
        n = len(num)
        max_len = 10
        def backtrack(start, sequence):
            if start == n and len(sequence) >= 3:
                return sequence
            
            for end in range(start + 1, min(start + max_len, n) + 1):
                segment = num[start:end]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) >= 2**31:
                    continue
                
                value = int(segment)
                if len(sequence) < 2:
                    res = backtrack(end, sequence + [value])
                    if res:
                        return res
                else:
                    if value == sequence[-1] + sequence[-2]:
                        res = backtrack(end, sequence + [value])
                        if res:
                            return res
            return []
        
        return backtrack(0, [])

"""
Time Complexity: O(n³)
Space Complexity: O(n)

"""