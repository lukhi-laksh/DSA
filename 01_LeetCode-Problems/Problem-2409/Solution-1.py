class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):

        start = max(self.countDays(arriveAlice), self.countDays(arriveBob))
        end = min(self.countDays(leaveAlice), self.countDays(leaveBob))

        return max(0, end - start + 1)

    def countDays(self, date):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(date[:2])
        day = int(date[3:])
        dayCount = 0

        for i in range(month - 1):
            dayCount += days[i]

        return dayCount + day