"""
Maximum Area of Longest Diagnal Rectangle
"""
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        dimensions = sorted(dimensions)
        d = {}
        for a,b in dimensions:
            d[((a**2 + b**2)**0.5)] = [a,b]
        c = max(d)
        a, b = d[c]
        return a*b
    

sol = Solution()
rectangles = [(3, 4), (5, 12), (8, 15), (7, 24)]

print(sol.areaOfMaxDiagonal(rectangles))
    
"""

Time Complexity:  O(n log n)
Space Complexity: O(n)

"""