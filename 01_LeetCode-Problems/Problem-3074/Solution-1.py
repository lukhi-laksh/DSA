"""
Apple Redistribution into box 

"""

class Solution(object):
    def minimumBoxes(self, apple, capacity):

        sm = sum(apple)  
        c = 0
       
        stack = capacity[:]   

        while sm > 0 and stack:
           
            max_idx = 0
            for i in range(1, len(stack)):
                if stack[i] > stack[max_idx]:
                    max_idx = i

         
            largest = stack.pop(max_idx)
            sm -= largest
            c += 1

            if sm <= 0:
                return c

        return -1

"""
Time Complexity: O(n²)
Space Complexity: O(n)

"""