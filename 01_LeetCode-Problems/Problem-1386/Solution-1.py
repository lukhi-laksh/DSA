"""
Cinema Seat Allocation

"""
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        reservedSeats.sort()
        rst = 0
        idx = 0
        row_count = 0
        while idx < len(reservedSeats):
            cur_row = reservedSeats[idx][0]
            l_valid = mid_valid = r_valid = True
            while idx < len(reservedSeats) and reservedSeats[idx][0] == cur_row:
                if 2 <= reservedSeats[idx][1] <= 3:
                    l_valid = False
                elif 4 <= reservedSeats[idx][1] <= 7:
                    mid_valid = False
                    if reservedSeats[idx][1] <= 5:
                        l_valid = False
                    if reservedSeats[idx][1] >= 6:
                        r_valid = False
                elif 8 <= reservedSeats[idx][1] <= 9:
                    r_valid = False
                idx += 1
            if l_valid and r_valid:
                rst += 2
            elif l_valid or r_valid or mid_valid:
                rst += 1
            row_count += 1
        return rst + (n - row_count) * 2

"""
Time Complexity:  O(m log m)
Space Complexity: O(m)

"""