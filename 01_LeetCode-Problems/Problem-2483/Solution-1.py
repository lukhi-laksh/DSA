"""
Docstring for 01_LeetCode-Problems.Problem-2483.py.Solution-1

"""

class Solution(object):
    def bestClosingTime(self, customers):

        left=[]
        for val in customers:
            if val == "Y" and left:
                left.append(left[-1])
            elif val == "Y":
                left.append(0)
            elif val == "N" and left:
                left.append(left[-1]+1)
            else:
                left.append(1)
        left.append(left[-1])
        right=[0]
        customers= list(customers)
        customers.reverse()
        for val in customers:
            if val =="N" and right:
                right.append(right[-1])
            elif val=="N":
                right.append(0)
            elif val =="Y" and right:
                right.append(right[-1]+1)
            else:
                right.append(1)
        right.reverse()
        ans = []
        for index in range(len(left)):
            if index!=0:
                ans.append(right[index]+left[index-1])
            else:
                ans.append(right[index])
        mini = min(ans)
        print(ans)
        for index,val in enumerate(ans):
            if mini == val:
                return index

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""