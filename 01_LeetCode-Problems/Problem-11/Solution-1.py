"""
Container with most Water

"""
class Solution(object):
    def maxArea(self, height):
        maxx = 0 
        i = 0
        j = len(height)-1
        while i < j:
            width = abs(i-j)
            area = width * min(height[i],height[j])
            maxx = max(area,maxx)
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return maxx 

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""