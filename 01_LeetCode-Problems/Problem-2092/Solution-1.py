"""
Find All People With Secret

"""

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key = lambda x:x[2])
        m = len(meetings)

        has_secret = set([0, firstPerson])

        i = 0
        while i < m:
            time = meetings[i][2]
            time_meetings = []
            while i < m and meetings[i][2] == time:
                time_meetings.append((meetings[i][0], meetings[i][1]))
                i += 1

            told_secret = True
            while told_secret:
                told_secret = False
                for x, y in time_meetings:
                    if x in has_secret and y not in has_secret:
                        has_secret.add(y)
                        told_secret = True
                    elif y in has_secret and x not in has_secret:
                        has_secret.add(x)
                        told_secret = True

        return list(has_secret)
    
"""
Time Complexity: O(m log m + m²)
Space Complexity: O(n + m)

"""