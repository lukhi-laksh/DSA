class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if(i in ["(","{","["]):
                stack.append(i)
            else:
                if(len(stack)==0):
                    return False
                if(i==")" and stack and stack[-1]=="("):
                    stack.pop(-1)
                elif(i=="]" and stack and stack[-1]=="["):
                    stack.pop(-1)
                elif(i=="}" and stack and stack[-1]=="{"):
                    stack.pop(-1)
                else:
                    break
        return len(stack)==0