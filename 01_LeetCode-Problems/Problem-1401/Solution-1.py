"""
Circle and Ractengle Overlapptin

"""
class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        nearX = max(x1, min(xCenter, x2))
        nearY = max(y1, min(yCenter, y2))

        diffX = xCenter - nearX
        diffY = yCenter - nearY

        return diffX * diffX + diffY * diffY <= radius * radius

"""
Time Complexity: O(1)
Space Complexity: O(1)

"""