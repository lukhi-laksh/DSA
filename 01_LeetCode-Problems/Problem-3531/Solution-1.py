"""
Count Covered Buldings

"""

from collections import defaultdict

class Solution(object):
    def countCoveredBuildings(self, n, buildings):

        ax0_to_ax1 = defaultdict(lambda: [float('inf'), -float('inf')])
        ax1_to_ax0 = defaultdict(lambda: [float('inf'), -float('inf')])

        for ax0, ax1 in buildings:
            ax0_to_ax1[ax0][0] = min(ax0_to_ax1[ax0][0], ax1)
            ax0_to_ax1[ax0][1] = max(ax0_to_ax1[ax0][1], ax1)
            ax1_to_ax0[ax1][0] = min(ax1_to_ax0[ax1][0], ax0)
            ax1_to_ax0[ax1][1] = max(ax1_to_ax0[ax1][1], ax0)

        total = 0

        for ax0, ax1 in buildings:
            min_ax1, max_ax1 = ax0_to_ax1[ax0]
            min_ax0, max_ax0 = ax1_to_ax0[ax1]

            if (ax1 != min_ax1 and ax1 != max_ax1 and
                ax0 != min_ax0 and ax0 != max_ax0):
                total += 1

        return total
    
"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""
