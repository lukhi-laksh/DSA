class Solution(object):
    def largestTriangleArea(self, points):
        n = len(points)
        max_area = 0
        i = 0
        while i < n :
            j = i+1 
            while j < n :
                k = j+1 
                while k < n :
                   x1, y1 = points[i]
                   x2, y2 = points[j]
                   x3, y3 = points[k]
                    
                   area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0
                   max_area = max(max_area, area)
                   k += 1
                j += 1
            i += 1
        return max_area