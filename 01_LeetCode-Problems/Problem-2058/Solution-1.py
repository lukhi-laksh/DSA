class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        critical=[];
        temp=head.next;
        prev=head;
        ind=1;
        while(temp and temp.next):
            if(prev.val<temp.val and temp.val>temp.next.val):
                critical.append(ind);
            elif(prev.val>temp.val and temp.val<temp.next.val):
                critical.append(ind);
            prev,temp=temp,temp.next;
            ind+=1;
        if(len(critical)<2):
            return [-1,-1];
        res=float("inf");
        for i in range(len(critical)-1):
            res=min(res,critical[i+1]-critical[i]);
        return [res,critical[-1]-critical[0]]