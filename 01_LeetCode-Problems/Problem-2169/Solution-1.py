class Solution(object):
    def countOperations(self, num1, num2):

        count = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
                count += 1
            else:
                num2 -= num1
                count += 1
        return count
            

        