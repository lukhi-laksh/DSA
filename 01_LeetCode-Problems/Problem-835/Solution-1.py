"""
Image Overlap

"""
class Solution(object):
    def largestOverlap(self, img1, img2):

        img1_ones = []
        img2_ones = []

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_ones.append((i, j))
                
                if img2[i][j] == 1:
                    img2_ones.append((i, j))

        shift_counts = defaultdict(int)
        max_overlap = 0

        for r1, c1 in img1_ones:
            for r2, c2 in img2_ones:
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] += 1
            
                max_overlap = max(max_overlap, shift_counts[shift])
        
        return max_overlap

"""
Time Complexity(n²)
Space Complexity(n)

"""