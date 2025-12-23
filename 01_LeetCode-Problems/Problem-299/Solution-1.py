"""
Bulls and Cows

"""

class Solution(object):
    def getHint(self, secret, guess):

        x,y=0,0
        m=set()
        n=set()
        for i in range(len(guess)):
            if guess[i]==secret[i]:
                x+=1
                m.add(i)

        for k in range(len(secret)):
            if k not in m and guess[k] in secret:
                for h in range(len(secret)):
                    if h not in n and h not in m and guess[k]==secret[h]:
                        y+=1
                        n.add(h)
                        break

        x=str(x)
        y=str(y)
        return x+"A"+y+"B"

"""
Time Complexity: O(n²)
Space Complexity: O(n)

"""