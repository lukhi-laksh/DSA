"""
Productof the Last K Numbers

"""
class ProductOfNumbers(object):
    def __init__(self):   
        self.input_array = []
        self.product = []
        
    def add(self, num):
        if num == 0:
            self.input_array = []
            self.product = []
            return
        self.input_array.append(num)
        if len(self.product) == 0:
            self.product.append(num)
        else:
            self.product.append(num*self.product[-1])

    def getProduct(self, k):
        start = len(self.input_array)-1
        result = 1
        if k > len(self.input_array):
            return 0
        elif k == len(self.input_array):
            return self.product[-1]
        result = self.product[-1] // self.product[start-k] 
        return result
"""
Time Complexity: O(1)
Space Complexity: O(n)

"""