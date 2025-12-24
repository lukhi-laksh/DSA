"""
Number of Boomengers
"""


from typing import Counter

class Solution(object):
    def numberOfBoomerangs(self, points):

        ans =0 
        for pivot in points:
            px,py = pivot
            freq = Counter()
            for end in points:
                ex,ey = end
                dx,dy = px-ex,py-ey
                d = dx**2+dy**2
                freq[d]+=1
            for v in freq.values():
                ans += v*(v-1)
        return ans

"""
Time Complexity: O(n²)
Space Complexity: O(n)

"""