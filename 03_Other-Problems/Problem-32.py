class Solution(object):
    def numberOfPairs(self, points):
        
        co = sorted(points, key=lambda x: (-x[1], x[0]))
        l=len(co)
        
        ans=0
                
        for i in range(l-1):
            for j in range(i+1,l):
                x1,x2=co[i][0],co[j][0]
                y1,y2=co[i][1],co[j][1]
                yes=True
                
                if y1>=y2 and x1<=x2:
                    for k in range(i+1,j):
                        if min(x1,x2)<=co[k][0]<=max(x1,x2) and min(y1,y2)<=co[k][1]<=max(y1,y2):
                            yes=False
                            break
                    if yes:
                        ans+=1
            
        
        return ans