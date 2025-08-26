class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        dimensions = sorted(dimensions)
        d = {}
        for a,b in dimensions:
            d[((a**2 + b**2)**0.5)] = [a,b]
        c = max(d)
        a, b = d[c]
        return a*b
        