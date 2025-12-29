"""
Pyramid Transiction Matrix

"""

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        mp = {}
        for rule in allowed:
            pair = rule[:2]
            top = rule[2]
            mp.setdefault(pair, []).append(top)

        memo = {}

        def build(row):
            if len(row) == 1:
                return True
            
            if row in memo:
                return memo[row]

            def generate_next(i, current):
                if i == len(row) - 1:
                    result.append("".join(current))
                    return
                
                pair = row[i:i+2]
                if pair not in mp:
                    return
                
                for ch in mp[pair]:
                    current.append(ch)
                    generate_next(i + 1, current)
                    current.pop()

            result = []
            generate_next(0, [])

            for nxt in result:
                if build(nxt):
                    memo[row] = True
                    return True

            memo[row] = False
            return False

        return build(bottom)
