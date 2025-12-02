"""
Count Number of Trapezoids I

"""



class Solution(object):
    def countTrapezoids(self, points):

        sorted(points, key=lambda p: p[1])

        N = len(points)
        ans = 0
        y_count = {}
        for i in range(N):
            if points[i][1] in y_count:
                y_count[points[i][1]] += 1
            else:
                y_count[points[i][1]] = 1

        y_line = []
        for (k, v) in y_count.items():
            if v >= 2:
                y_line.append(v * (v-1) / 2)

        cur = 0
        for i in range(len(y_line)):
            ans += cur * y_line[i]
            ans = ans % 1000000007
            cur += y_line[i] 
            cur = cur % 1000000007
        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""