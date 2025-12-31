"""
Finding the users Active Minutes

"""


class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        userMinutesMapper = dict()
        for log in logs:
            if log[0] not in userMinutesMapper:
                userMinutesMapper[log[0]] = { log[1] }
            else:
                userMinutesMapper[log[0]].add(log[1])
        
        userActiveMinutes = [0]*k
        for activeMinute in userMinutesMapper.values():
            userActiveMinutes[len(activeMinute)-1] += 1

        return userActiveMinutes
    
"""
Time Complexity: O(n)
Space Complexity: O(n)

"""