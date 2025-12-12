"""
Count Mentions Per User

"""

class Solution(object):
    def countMentions(self, numberOfUsers, events):

        mentions = [0]*(numberOfUsers)
        online = [True]*(numberOfUsers)
        onlinets = [0]*(numberOfUsers)
        n = len(events)
        for i in range(n):
            for j in range(n-i-1):
                if(int(events[j][1])>int(events[j+1][1])):
                    temp = events[j]
                    events[j] = events[j+1]
                    events[j+1]=temp
                if(int(events[j][1])==int(events[j+1][1])):
                    if(events[j+1][0]=="OFFLINE"):
                        temp = events[j]
                        events[j] = events[j+1]
                        events[j+1]=temp
        for i in range(n):
            for t in range(numberOfUsers):
                if((int(events[i][1])-onlinets[t]) >= 60):
                    online[t] = True
            if(events[i][0]=="OFFLINE"):
                onlinets[int(events[i][2])] = int(events[i][1])
                online[int(events[i][2])] = False
            elif(events[i][0]=="MESSAGE"):
                if(events[i][2]=="ALL"):
                    for t in range(len(mentions)):
                        mentions[t]+=1
                elif(events[i][2]=="HERE"):
                    for t in range(numberOfUsers):
                        if online[t]==True:
                            mentions[t]+=1
                else:
                    userlist = events[i][2].split()
                    for j in range(len(userlist)):
                        userid = userlist[j][2:]
                        mentions[int(userid)]+=1
        return mentions

"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""