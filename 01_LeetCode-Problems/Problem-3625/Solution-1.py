"""
Count Number of Trapezpids II
"""

class Solution(object):

    def countTrapezoids(self, points):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(points)
        from collections import defaultdict
        
        slope_to_lines = defaultdict(lambda: defaultdict(list))
        
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx, dy = xj - xi, yj - yi
                
                if dx == 0:
                    slope = (1, 0)
                    line = xi
                elif dy == 0:
                    slope = (0, 1)
                    line = yi
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx, dy = dx // g, dy // g
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dy, dx)
                    line = dx * yi - dy * xi
                
                slope_to_lines[slope][line].append((i, j))
        
        total = 0
        
        for slope, lines_dict in slope_to_lines.items():
            lines_list = list(lines_dict.values())
            num_lines = len(lines_list)
            
            if num_lines < 2:
                continue
            
            for idx1 in range(num_lines):
                for idx2 in range(idx1 + 1, num_lines):
                    seg_count1 = len(lines_list[idx1])
                    seg_count2 = len(lines_list[idx2])
                    total += seg_count1 * seg_count2
        
        midpoint_to_segments = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                mx = points[i][0] + points[j][0]
                my = points[i][1] + points[j][1]
                midpoint_to_segments[(mx, my)].append((i, j))
        
        parallelogram_count = 0
        for segments in midpoint_to_segments.values():
            if len(segments) >= 2:
                for i in range(len(segments)):
                    for j in range(i + 1, len(segments)):
                        p1, p2 = segments[i]
                        p3, p4 = segments[j]
                        x0, y0 = points[p1]
                        x1, y1 = points[p2]
                        x2, y2 = points[p3]

                        if (y1 - y0) * (x2 - x0) != (y2 - y0) * (x1 - x0):
                            parallelogram_count += 1
        
        return total - parallelogram_count
    
"""
Time Complexity: O(n²)
Space Complexity: O(n²)

"""