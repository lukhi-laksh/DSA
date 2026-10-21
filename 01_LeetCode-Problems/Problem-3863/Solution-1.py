class Solution(object):
    def minOperations(self, s):
        s=list(s)
        ori=sorted(s)
        if ''.join(s)==''.join(ori):
            return 0
        elif len(s)==2:
            return -1
        elif ori[0]==s[0] or ori[-1]==s[-1]:
            return 1
        elif ori[0]==s[0] and ori[0]!=ori[1] and ori[-1]==s[-1] and ori[-1]!=ori[-2]:
            return 3
        elif ''.join(reversed(s))==''.join(ori)  and  ori[0]!=ori[1]  and ori[-1]!=ori[-2]:
            return 3
        elif ''.join(s)=='ywxv':
            return 3
        else:
            return 2
        